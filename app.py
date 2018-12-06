#引用套件
from flask import Flask, request, abort



from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,LineBotApiError
)
from linebot.models import *


import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('ZD2oeQC2yTeiStCvFgLhCbeO4XrwALUYZkmvtpS+1qCzRt7jTwbo1qe7Y1e4z3IdCNMnVfZefN81QEjhJj9sHVbqD0CCQlfZVra3UVfr8ufPYsxwKe4ts+PC+k6SRKzMVFSzDPN+cmpxHuXErf+1FQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('7b3daf73b5fe9358c1085d2cb8dd01d7')




#  /callback  Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


def Dcard():
    url = 'https://www.dcard.tw/f'
    resp = requests.get(url)
    #HTTP 
    print(resp.status_code)
    #  Beautiful Soup 
    soup = BeautifulSoup(resp.text, 'html.parser')
    # print(soup.prettify())
    dcard_title = soup.find_all('h3', re.compile('PostEntry_title_'))

    for index, item in enumerate(dcard_title[:10]):
        content += '{0:2d}. {1}\n'.format(index + 1, item.text.strip())
        #print("{0:2d}. {1}".format(index + 1, item.text.strip()))
    return content


def movie():
    target_url = 'https://movies.yahoo.com.tw/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('div.movielist_info h1 a')):
        if index == 20:
            return content       
        title = data.text
        link =  data['href']
        content += '{}\n{}\n'.format(title, link)
    return content

def CS():           
    message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/zh/thumb/6/63/National_Pingtung_University_logo.svg/1200px-National_Pingtung_University_logo.svg.png',
                        title='國立屏東大學_資訊科學系',
                        text='本系致力於智慧雲端系統與應用開發之研發工作',
                        actions=[
                            PostbackTemplateAction(
                                label='系所簡介',
                                text='系所簡介',
                                data='action=buy&itemid=1'
                            ),
                            MessageTemplateAction(
                                label='教學師資',
                                text='教學師資'
                            ),
                            MessageTemplateAction(
                                label='研究所',
                                text='研究所'
                            ),
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/zh/thumb/6/63/National_Pingtung_University_logo.svg/1200px-National_Pingtung_University_logo.svg.png',
                        title='國立屏東大學_資訊科學系',
                        text='本系致力於智慧雲端系統與應用開發之研發工作',
                        actions=[
                            PostbackTemplateAction(
                                label='實驗室',
                                text='實驗室',
                                data='action=buy&itemid=1'
                            ),
                            MessageTemplateAction(
                                label='大學部',
                                text='大學部'
                            ),
                            MessageTemplateAction(
                                label='未來學生',
                                text='未來學生'
                            ),
                        ]
                    ),
                ]
            )
        )
    return message

def CSIntroduction():
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://example.com/image.jpg',
        title='系所簡介',
        text='你可以問我',
        actions=[
            PostbackTemplateAction(
                label='系所介紹',
                text='系所介紹',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='發展特色',
                text='發展特色'
            ),
            MessageTemplateAction(
                label='未來發展',
                text='未來發展'
            )
        ]
    )
)
    return message
    
    





    
    
  

# 回應訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 
    #line_bot_api.push_message('Ubc4902b9b76350b957769c5376e7f43c',TextSendMessage(text=''))
    if event.message.text == "CS": 
        message=CS()
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == "系所簡介": 
        message = CSIntroduction()
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == "教學師資": 
        message = TextSendMessage(text='True')
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == "研究所": 
        message = TextSendMessage(text='True')
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == "實驗室": 
        message = TextSendMessage(text='True')
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == "大學部": 
        message = TextSendMessage(text='True')
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == "未來學生": 
        message = TextSendMessage(text='True')
        line_bot_api.reply_message(event.reply_token, message)


    if event.message.text == "系所介紹": 
        message = TextSendMessage(text='True')
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == "發展特色": 
        message = TextSendMessage(text='True')
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == "未來發展": 
        message = TextSendMessage(text='True')
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text == "Dcard":
        a=Dcard()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=a))
    
    if event.message.text == '==':
        message = TextSendMessage(text='fuck')
        line_bot_api.reply_message(event.reply_token,message)
    elif event.message.text =='location':
       message = LocationSendMessage(
           title='my location',
           address='Tokyo',
           latitude=35.65910807942215,
           longitude=139.70372892916203
       )
       line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token, message)

    

    


    

    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)




