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
        text = f'[+]BC4T (Nuwan Konara) \n\n*Menu :*  \n\n<url> : Youtube Downloader\n\n <url> : Facebook Downloader \n\n *TRS* _<Text>_ : Translate to English to Sinhala\n\n *TRE* _<Text>_ : Translate Sinhala To English\n\n*pypdf*: Python Pdf set\n\n*dow* _<link>_ : download media items\n\n*cal* _<expression>_ : Calculator\n\n<tiktok_url> : TIKTOK VIDEO DOWNLOADER'
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
    if 'tiktok' in incoming_msg:
        import requests
        import json 
        urls=incoming_msg
        url="https://api.tiktokmultidownloader.com/v1/get?url="+urls
        res=requests.get(url)
        link=res.text
        real_res = json.loads(link) 
        msg.media(real_res['data']['video']['url'])
    if "yttt" in incoming_msg:
        msg.body("https://ljs.ijjiii.is/c5a5d4a06b5b07a6c12c6ba0b2dac22d/TY3yxcIyFl8/crnxcnrxmoxsn")
        
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
