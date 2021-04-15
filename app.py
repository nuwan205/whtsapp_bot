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
        text = f'[+]BC4T (Nuwan Konara) \n\n*/Menu :*  \n\n/yb<url> : Youtube Downloader\n\n /fb<url> : Facebook Downloader \n\n */TS* _<Text>_ : Translate to English to Sinhala\n\n */TE* _<Text>_ : Translate Sinhala To English\n\n*/pypdf*: Python Pdf set\n\n*/dw* _<link>_ : download media items\n\n*/cl* _<expression>_ : Calculator\n\n<tiktok_url> : TIKTOK VIDEO DOWNLOADER\n\n*/sy* _<words>_ : Youtube search\n\n*/ya*_<yt_url> : Yt Audio Downloder\n\n*/sd* <movie name> : Sinhala Subtitle downloader\n\n*/ml* <movie name> : Movie Links \n\n*/mu*  : Top Newest Movie List'
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

    if "yyy" in incoming_msg:
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
    if '/sd' in incoming_msg:
        from googlesearch import search
        from bs4 import BeautifulSoup as bs
        from requests_html import HTMLSession
        session = HTMLSession()

        search=search(incoming_msg[3:]+"sinhala subtitle download piratelk", num_results=1)
        print(search)
        if 'pirate' in search[0]:
            print(search[0])
            res = session.get(search[0])
            final = res.text
            soup =  bs(final, 'html.parser')
            try:
                result_block = soup.find_all('a', attrs={'class': 'aligncenter'})
                result=str(result_block[0]).split(" ")
                final=result[3].replace("href=","")
                msg.body(final)
            except:
                msg.body("An error has encountered!")
        else:
            msg.body("Sorry subtitle is not available for some old movies!!!")
    if "/ml" in incoming_msg:
        from googlesearch import search
        from bs4 import BeautifulSoup as bs

        from requests_html import HTMLSession
        session = HTMLSession()



        search=search("piratelk.com"+incoming_msg[3:], num_results=1)
        print(search)
        if 'pirate' in search[0]:
            print(search[0])
            res = session.get(search[0])
            final = res.text
            soup =  bs(final, 'html.parser')
            print(type(soup))
            try:
            
                result_block = soup.find_all('a', attrs={'class': 'su-button su-button-style-default'})
                if len(result_block)==0:
                    result_links=soup.find_all('p')
                    links_li=[]
                    for i in result_links:
                        links = i.find_all('a',attrs={"rel":"noopener noreferrer"})
                        servers=["https://racaty.net","https://megaup.net","https://clicknupload.org","https://drive.google.com","https://mega.nz","https://usersdrive.com","verystream.com"]
    
                        for i in links:
                            for x in servers:
                                v=0
                                if x in str(i):
                                    i=str(i).split(" ")[1].replace("href=","")
                                    you = f'__________Movie Links----------\n\n *LINK* : '+str(i)
                                    print(you)
                                    msg.body(you)
                                    v+=1
                                    
                                    if v>=6:
                                        break
                else:
                    v=0
                    for i in result_block:
                        i=str(i).replace('rel="noopener noreferrer" style="color:#FFFFFF;background-color:#2D89EF;border-color:#246ec0;border-radius:5px;-moz-border-radius:5px;-webkit-border-radius:5px" target="_blank"><span style="color:#FFFFFF;padding:6px 16px;font-size:13px;line-height:20px;border-color:#6cadf4;border-radius:5px;-moz-border-radius:5px;-webkit-border-radius:5px;text-shadow:none;-moz-text-shadow:none;-webkit-text-shadow:none"><i class="sui sui-arrow-circle-down" style="font-size:13px;color:#FFFFFF"></i> ',"")
                        i=i.split(" ")[3].replace("href=","")+i.split(" ")[4]+i.split(" ")[5]
                        you = f'__________Movie links----------\n\n *LINK* : '+i
                        print(you)
                        msg.body(you)
                        v+=1
                        if v>=6:
                            break
            except:
                msg.body("An error has encountered")

        else:
            msg.body("Sorry some links is not available for some old movies!!!")
    if "/mu" in incoming_msg:
        from googlesearch import search
        from bs4 import BeautifulSoup as bs

        from requests_html import HTMLSession
        session = HTMLSession()


        res = session.get("https://piratelk.com/category/%E0%B7%84%E0%B7%9C%E0%B6%B3%E0%B6%B8-%E0%B6%A0%E0%B7%92%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%B4%E0%B6%A7/")
        final = res.text
        soup =  bs(final, 'html.parser')
        links = soup.find_all('h2',attrs={"class":"post-box-title"})
        for i in links:
            i=str(i).split('/">')[1].replace("</a>\n</h2>","")
            you = f'__________TOP Movie list----------\n\n *Yeah Boy* : '+i
            msg.body(you)
    if "/dt" in incoming_msg:
        from bs4 import BeautifulSoup as bsp
	
        from requests import get

        from random import choice

        words = []

        def req_soup(search):
	        html = get('https://www.maduraonline.com',params={'find':search}).text
	        
	        soup = bsp(html,'html.parser')
		    global soup
        def is_res():
	        if soup.find('p',class_='pt'):
		        for i in soup.find_all('td',class_='td'):
			        words.append(i.text)
		        return False
	        else:
		        return True
        def res_scrape():
	        for i in soup.find_all('td',class_='td'):
		        if i.text.strip():
			        words.append(i.text.strip())

        def main():
	        try:
	
		        search = incoming_msg[3:]
		        req_soup(search)
		        if is_res():
			        res_scrape()
			        print(' [+] Results For Your Search: ')
			        for i in enumerate((words),start=1):
				        print(str(i[0])+'.'+i[1])
		        else:
			        print('[!] No Results')
			

	        except KeyboardInterrupt:
		        exit()
        
        main()

    
    





    return str(resp)
if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
