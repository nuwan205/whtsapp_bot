from flask import Flask, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse

glo_links=""
app = Flask(__name__)





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



    
    def links(incoming_msg):
        global glo_links
        import requests as r
        import json
        print("hello")
        url="https://yt1s.com/api/ajaxSearch/index"
        link=incoming_msg[3:]
        glo_links=link
   
        data={"q":link+"=home"}
  
        res=r.post(url,data=data)
        links=res.text
        links= json.loads(links)
        conv_url="https://yt1s.com/api/ajaxConvert/convert"
        x=""
        for i in (links['links']['mp4']):
            link=links['links']['mp4'][i]
            
            x+=","+link['q']+"-"+link['size']
            
     
        y=x.replace(",","\n")
        z=y+"\n\nInput the quality Ex:1080p"
        msg.body(y)
       
    def down(p):
        global glo_links
        import requests as r
        import json
    
        print(p)
        link=glo_links
        glo_links=""
        print(link)
        data={"q":link+"=home"}
        print(data['q'])
        url="https://yt1s.com/api/ajaxSearch/index"
        res=r.post(url,data=data)
        links=res.text
        links= json.loads(links)
        conv_url="https://yt1s.com/api/ajaxConvert/convert"
        for i in (links['links']['mp4']):
            link=links['links']['mp4'][i]
            if link['q']==p:
                data={"vid":links['vid'],"k":link['k']}
                res = r.post(conv_url,data=data)
                down=res.text
                down_link=json.loads(down)
                x=down_link['dlink']
                print(x)
                msg.body(x)
                responded=True
            else:
                continue
           


    if 'YOU' in incoming_msg.upper():
        links(incoming_msg)
        print(glo_links)

    if '720p' in incoming_msg.lower():
        down(incoming_msg)
    

    if '1080p' in incoming_msg.lower():
        down(incoming_msg)
    

    if '480p' in incoming_msg.lower():
        down(incoming_msg)
    

    if '360p' in incoming_msg.lower():
        down(incoming_msg)

    if '240p' in incoming_msg.lower():
        down(incoming_msg)
    
    if '144p' in incoming_msg.lower():
        down(incoming_msg)
   
        












    return str(resp)
if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
