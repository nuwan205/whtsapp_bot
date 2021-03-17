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
        text = f'[+]BC4T (Nuwan Konara) \n\n*Menu :*  \n\n/yb<url> : Youtube Downloader\n\n /fcb<url> : Facebook Downloader \n\n *TRS* _<Text>_ : Translate to English to Sinhala\n\n *TRE* _<Text>_ : Translate Sinhala To English\n\n*pypdf*: Python Pdf set\n\n*dow* _<link>_ : download media items\n\n*cal* _<expression>_ : Calculator\n\n<tiktok_url> : TIKTOK VIDEO DOWNLOADER'
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
    if '$test' in incoming_msg:
        msg.body("ouliy6qhr0.1000traffics.com/gv?a=11365&d=ATwNOuXhsy6mp8cjwMlNL41inOkmwwGg8nZhUIce8Um0jnqZX4Xabgedd6F8uvRvuJOOU7ZGd0uhL3rCr6tut4iRfkeu7PPAImY-oovsFy1s3ow-a1p52tkB67ZwWqtfdRM_MuJ1iPY8AomWSiTlsryBAX9oHLe7342YQamY2dz-HP4iI4z0bht_1HweKuxiHMI0A65njsvh_1IELZVXRF7Dp8yJtLghDzh7boIp6S6zScNJSk6BOIzC4Yvt5_n6L61oX2UNvtaI5Nn4C7NMFbKfzO32Xgoif4iWc5YPyBqyKyVbSjuvektT4K7iJbtD5V1erEx9pgR4Elq4hUuZUCLP7p8DdmqSDrUhlLmztV7Tl-fY9hy6NEoN1UU-D1V1wzKvTbHTzXeGA46HLBUJx-ya78KXerB_LGMYAAPITw3e4N_vmViXyF89Cb4xof7Cf5goKdxiPZ1JcoaZ434qsYfSTCuZXYunsyzouw1koNPwgIvCYUjwekdrzX6ZTYuty4fWbQkmz8NkxoRRD5cTlZbCBQhcXlcABhXRJZai8sWSVKahxw6W24BB1G5LdAPBHFo48MZF9eMQFTY-lxluJjiOtRSSObYHxQ5Hc2mG3n3rq5y3v4-vpkpBVNhRg-1_4wASUjHxoWbNrKgamcJhuM388q8aaNPwAUUGX92fY0EHGuUC5zf8hBIpWIYM_447EandKAjhG7DXMzsxh2Bxi9-bxhfbT1d1Sq48AuGX8_-15i1dWVcrJWFZZFpRDtjolfKOuDzblKouiXI3DJUNtWK2KXaNVdtnDDRslqwxJLa38wdbfqvUrue6GORaJ3qisCrEuznKcMyURXir_VriSZzshPM9HR_xQRp1CxaPfIHzrd8M2K_7sO5_5xvpUz2_JqmXXhIn_NLewui3NwqWE1e5ylcgWqQHF3xZPzKF0Bknt42uBD50AwWtlnFBJ5RdPY-Tm0NilYGpOPK7onX5scOAAOr5lrM01h5vvBL2vXxjSYwHDfRXkA7gFFyG2-RpEul1xt7ANlgbV2BzONTKX9D9HHlIRsd3d3mW_4DRRY5A7LWwefXEl2FJBgnBhj7Jcb47CNo9FVuFwHrEufOMimTgbcuX-BkqpPpuTxGGjM6lYVJ8Y-ycV_-N7JI1r-2w")
    
        
      








    return str(resp)
if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
