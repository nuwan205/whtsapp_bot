from flask import Flask, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse

glo_links=""
app = Flask(__name__)

@app.route("/")
def hello():
    return "Status Online"

@app.route("/yt_down")
def yt_down():
    import pafy
    import requests as r
    par = "https://youtu.be/2Jub_HS-_0c"
    audio = pafy.new(par)
    x=audio.streams
    x[0].download()



@app.route('/bot', methods=['GET','POST'])
def bot():
 
    incoming_msg = request.values.get('Body', '')

    resp = MessagingResponse()
    msg = resp.message()

    responded = True

    if 'start' in incoming_msg.lower():
        text = "Helo how are you:::::Type menu for more"
        print(dir(msg))
        for i in i:
            msg.body(i)
            responded = True

    if 'menu' in incoming_msg.lower():
        text = f'[+]BC4T (Nuwan Konara) \n\n*Menu :*  \n\n<url> : Youtube Downloader\n\n <url> : Facebook Downloader \n\n *TRS* _<Text>_ : Translate to English to Sinhala\n\n *TRE* _<Text>_ : Translate Sinhala To English\n\n*pypdf*: Python Pdf set\n\n*dow* _<link>_ : download media items\n\n*cal* _<expression>_ : Calculator'
        msg.body(text)
        responded = True

    if 'https://www.facebook.com' in incoming_msg.lower():
        import requests as r
        import re
        par = incoming_msg
        html = r.get(par)
        video_url = re.search('sd_src:"(.+?)"', html.text).group(1)
        msg.body(video_url)
        responded = True
    if 'https://youtu.be' in incoming_msg.lower():
        
        from pytube import YouTube
        link = incoming_msg
        yt = YouTube(link)
        print("Title: ",yt.title)
        print("Length of video: ",yt.length)
        ys = yt.streams.filter(progressive=True,file_extension='mp4').get_highest_resolution()
        x=ys.url
        print(x)
        msg.body(x)
    if 'TRS' in incoming_msg.upper():
        from google_trans_new import google_translator
        translator = google_translator()  
        translate_text = translator.translate(incoming_msg[3:],lang_src='en', lang_tgt='si')  
        print(translate_text)
        msg.body(translate_text)
    if 'TRE' in incoming_msg.upper():
        from google_trans_new import google_translator
        translator = google_translator()  
        translate_text = translator.translate(incoming_msg[3:],lang_src='si', lang_tgt='en')  
        print(translate_text)
        msg.body(translate_text)
    if 'CAL' in incoming_msg.upper():
        num=str(incoming_msg[3:])
        if "÷" in num:
            num=num.replace("÷","/")
        x=eval(num)
        final=str(x)
        msg.body(final)
    if 'yt' in incoming_msg:
        msg.body("https://r6---sn-qp5avb5mp5u5-jhcs.googlevideo.com/videoplayback?expire=1615906478&ei=TnJQYPDHLM2rkwa474nwCw&ip=107.161.26.190&id=o-AC0QY7q_jlbXOJAzNXWrHQbWj-V0V35hxF_5OFy_p25Y&itag=18&source=youtube&requiressl=yes&vprv=1&mime=video%2Fmp4&ns=fWTwZlywDSNIaaQswC8vJScF&gir=yes&clen=46890679&ratebypass=yes&dur=1625.025&lmt=1609115642813151&fvip=3&fexp=24001374%2C24007246&c=WEB&txp=5432434&n=-mSB_5APXwC2182mdi&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgIdxMHx7U7pLfLGFF1AUZSo-vHKefCawBxUTyKaIzIqACIQDU_n00VbMt64z527Kj0EN423W-qWxMjsBvj2aGlfkXOg==&title=RanidU+Most+HitS+Songs+%E2%9D%A4%EF%B8%8F+%7C+Hard+Bass+%26+Hight+Quality&cms_redirect=yes&mh=FN&mip=2402:4000:2381:1967:56c9:1e77:41b4:2e2&mm=31&mn=sn-qp5avb5mp5u5-jhcs&ms=au&mt=1615884756&mv=m&mvi=6&pl=45&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIhAO8XeYr5WMSH-Mh6l89_hH_HXbgEw-WXUOOZcUSmChFUAiA3np5TrBcl0wSXUKbRU9lj4vFna0Jrzqtb7D1Br0suYg%3D%3D")
        
    if 'pypdf' in incoming_msg.lower():
        from googlesearch import search
        query = "http://index-of.es/Python/"
    
        for i in search(query,10):
            if ".pdf" in i:
                text = f'__________PYPDFS----------\n\n *LINK* : '+i
               
                msg.body(text)
                
                
    if 'dow' in incoming_msg.lower():
        x=incoming_msg[3:]
        msg.media(x)
    
        
      








    return str(resp)
if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
