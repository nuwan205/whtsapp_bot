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
        i="1","2","4"
        for i in i:
            msg.body(i)
            responded = True

    if 'menu' in incoming_msg.lower():
        text = f'[+]BC4T (Nuwan Konara) \n\n*Menu :*  \n\n*YOU* _<url>_ : Youtube Downloader\n\n *FB* _<url>_ : Facebook Downloader\n\n'
        msg.body(text)
        responded = True

    if 'fb' in incoming_msg.lower():
        import requests as r
        import re
        par = incoming_msg[2:]
        html = r.get(par)
        video_url = re.search('sd_src:"(.+?)"', html.text).group(1)
        msg.body(video_url)
        responded = True
    if 'YOU' in incoming_msg:
        
        from pytube import YouTube
        link = incoming_msg[3:]
        yt = YouTube(link)
        print("Title: ",yt.title)
        print("Length of video: ",yt.length)
        ys = yt.streams.filter(progressive=True,file_extension='mp4').get_highest_resolution()
        x=ys.url
        print(x)
        msg.media(x)
       
        print("Download completed!!")









    return str(resp)
if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
