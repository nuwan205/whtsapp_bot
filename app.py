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

    if '/menu' in incoming_msg.lower():
        text = f'[+]BC4T (Nuwan Konara) \n\n*/Menu :*  \n\n/yb<url> : Youtube Downloader\n\n /fb<url> : Facebook Downloader \n\n */TS* _<Text>_ : Translate to English to Sinhala\n\n */TE* _<Text>_ : Translate Sinhala To English\n\n*/pypdf*: Python Pdf set\n\n*/dw* _<link>_ : download media items\n\n*/cl* _<expression>_ : Calculator\n\n<tiktok_url> : TIKTOK VIDEO DOWNLOADER\n\n*/sy* _<words>_ : Youtube search\n\n*/ya*_<yt_url> : Yt Audio Downloder'
        msg.body(text)
        responded = True

    if '/fb' in incoming_msg.lower():
        import requests as r
        import re
        par = incoming_msg[3:]
        html = r.get(par)
        video_url = re.search('sd_src:"(.+?)"', html.text).group(1)
        msg.body(video_url)
        responded = True
    if '/yb' in incoming_msg.lower():
        
        from pytube import YouTube
        link = incoming_msg[3:]
        yt = YouTube(link)
        print("Title: ",yt.title)
        print("Length of video: ",yt.length)
        ys = yt.streams.filter(progressive=True,file_extension='mp4').get_highest_resolution()
        x=ys.url
        print(x)
        msg.body(x)
    if '/TS' in incoming_msg.upper():
        from google_trans_new import google_translator
        translator = google_translator()  
        translate_text = translator.translate(incoming_msg[3:],lang_src='en', lang_tgt='si')  
        print(translate_text)
        msg.body(translate_text)
    if '/TE' in incoming_msg.upper():
        from google_trans_new import google_translator
        translator = google_translator()  
        translate_text = translator.translate(incoming_msg[3:],lang_src='si', lang_tgt='en')  
        print(translate_text)
        msg.body(translate_text)
    if '/CL' in incoming_msg.upper():
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
    if "/yts1" in incoming_msg:
        import requests
        import json
        url_part=incoming_msg[3:]
        url_part=url_part.split("/")[-1]
        url="https://api3.youtube-mp3.org.in/@video/"+url_part+"?bypass=false&bypass2=false"
        res=requests.get(url)
        output=res.text
        res = json.loads(output)
        x=res['url']
        x=x.replace("status","download")
        msg.body(x)
        
    if '/pypdf' in incoming_msg.lower():
        from googlesearch import search
        query = "http://index-of.es/Python/"
    
        for i in search(query,10):
            if ".pdf" in i:
                text = f'__________PYPDFS----------\n\n *LINK* : '+i
               
                msg.body(text)
                
                
    if '/dw' in incoming_msg.lower():
        x=incoming_msg[3:]
        msg.media(x)
    if '$test' in incoming_msg:
        from selenium import webdriver
        GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
        CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
        chrome_options = webdriver.ChromeOptions()chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')chrome_options.binary_location = GOOGLE_CHROME_PATH
        
        browser = webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
        msg.body("ok")




        browser.get("https://www.google.com")
        print(browser.page_source)
    if "yy" in incoming_msg:
        msg.body("ok")
    if '/ya' in incoming_msg.lower():
        import requests
        msgs=incoming_msg[3:].split("/")[-1]
        url="https://mp3fy.com/yp/"+msgs
        msg.media(url)
    if '/sy' in incoming_msg.lower():
        from youtubesearchpython import VideosSearch
        topic=incoming_msg[3:]
        videosSearch = VideosSearch(topic, limit = 3)

        result=videosSearch.result()
        for i in result['result']:
            link=i['link'].split("=")[-1]
            real_link="https://youtu.be/"+link
            you = f'__________YTLINKS----------\n\n *LINK* : '+real_link
            msg.body(you)
   
            

        
      








    return str(resp)
if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
