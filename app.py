from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,LineBotApiError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('ZD2oeQC2yTeiStCvFgLhCbeO4XrwALUYZkmvtpS+1qCzRt7jTwbo1qe7Y1e4z3IdCNMnVfZefN81QEjhJj9sHVbqD0CCQlfZVra3UVfr8ufPYsxwKe4ts+PC+k6SRKzMVFSzDPN+cmpxHuXErf+1FQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('7b3daf73b5fe9358c1085d2cb8dd01d7')




# 監聽所有來自 /callback 的 Post Request
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

#追蹤
@handler.add(FollowEvent)
def handle_follow(event):
    print("in Follow")
    button_template_message =ButtonsTemplate(
                                    thumbnail_image_url="https://i.imgur.com/eTldj2E.png?1",
                                    title='Menu', 
                                    text='歡迎follow',
                                    image_size="cover",
                                    actions=[
                                        MessageTemplateAction(
                                            label='功能1', text='function-1'
                                        ),
                                        MessageTemplateAction(
                                            label='功能2', text='function-2'
                                        ),
                                        MessageTemplateAction(
                                            label='功能3', text='function-3'
                                        ),
                                    ]
                                )
                                
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text="Follow Event",
            template=button_template_message
        )
    )

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 推送訊息
    #line_bot_api.push_message('Ubc4902b9b76350b957769c5376e7f43c',TextSendMessage(text='我是基德 是名機器人'))

    # 回應訊息

    #圖片訊息
    if event.message.text== '圖片' :
        message = ImageSendMessage(
        original_content_url='',
        preview_image_url=''
        )
        line_bot_api.reply_message(event.reply_token, message)
    

    elif event.message.text == '==':
        message = TextSendMessage(text='終於有人知道= =中間不要加空格')
        line_bot_api.reply_message(event.reply_token,message)

    #影片訊息
    elif event.message.text =='影片':
        message = VideoSendMessage(
            original_content_url='https://example.com/original.mp4',
            preview_image_url='https://example.com/preview.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)

    #位置訊息
    elif event.message.text =='位置':
       message = LocationSendMessage(
           title='my location',
           address='Tokyo',
           latitude=35.65910807942215,
           longitude=139.70372892916203
       )
       line_bot_api.reply_message(event.reply_token, message)

    #組圖訊息
    elif event.message.text == '組圖':
        message = ImagemapSendMessage(
            base_url='https://example.com/base',
            alt_text='this is an imagemap',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                URIImagemapAction(
                    link_uri='https://example.com/',
                    area=ImagemapArea(
                        x=0, y=0, width=520, height=1040
                    )
                ),
                MessageImagemapAction(
                    text='hello',
                    area=ImagemapArea(
                        x=520, y=0, width=520, height=1040
                    )
                )
           ]
        )
        line_bot_api.reply_message(event.reply_token, message)

    #按鈕介面
    #elif event.message.text =='按鈕介面訊息':
    #    message = TemplateSendMessage(
    #        alt_text='Buttons template',
    #        template=ButtonsTemplate(
    #            thumbnail_image_url='https://example.com/image.jpg',
    #            title='Menu',
    #            text='Please select',
    #            actions=[
    #                PostbackTemplateAction(
    #                    label='postback',
    #                    text='postback text',
    #                    data='action=buy&itemid=1'
    #                ),
    #                MessageTemplateAction(
    #                    label='message',
    #                    text='message text'
    #                ),
    #               URITemplateAction(
    #                    label='uri',
    #                    uri='http://example.com/'
    #                )
    #           ]
    #        )
   # )
   # line_bot_api.reply_message(event.reply_token, message)
    

    else:
        message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token, message)

  
  
    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



#爬蟲（尚未確認功能，需測試回傳）
#引入函式庫
import requests 
import json
import datetime
import re

from selenium import webdriver
from bs4 import BeautifulSoup
from linebot import LineBotApi
from linebot.models import TextSendMessage

#dcard
url = 'https://www.dcard.tw/f'
resp = requests.get(url)
#HTTP 要求是否已經被完成
print(resp.status_code)
# 以 Beautiful Soup 解析 HTML 程式碼
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup.prettify())
dcard_title = soup.find_all('h3', re.compile('PostEntry_title_'))
print('Dcard 熱門前十文章標題：')
for index, item in enumerate(dcard_title[:10]):
    print("{0:2d}. {1}".format(index + 1, item.text.strip()))


# 下載 Yahoo 首頁內容
r = requests.get('https://tw.yahoo.com/')

# 確認是否下載成功
if r.status_code == requests.codes.ok:
  soup = BeautifulSoup(r.text, 'html.parser')

  # 以 CSS 的 class 抓出各類頭條新聞
  stories = soup.find_all('a', class_='story-title')
  for s in stories:
    # 新聞標題
    print("標題：" + s.text)
    # 新聞網址
    print("網址：" + s.get('href'))


# Google 搜尋 URL
google_url = 'https://www.google.com.tw/search'

# 查詢參數
my_params = {'q': 'example'}

# 下載 Google 搜尋結果
r = requests.get(google_url, params = my_params)

if r.status_code == requests.codes.ok:
  soup = BeautifulSoup(r.text, 'html.parser')

  # 觀察 HTML 原始碼
  # print(soup.prettify())

  # 以 CSS 的選擇器來抓取 Google 的搜尋結果
  items = soup.select('div.g > h3.r > a[href^="/url"]')
  for i in items:
    # 標題
    print("標題：" + i.text)
    # 網址
    print("網址：" + i.get('href'))    

#氣象
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import datetime
import os
import pyodbc

# 抓現在時間
today = str(datetime.date.today())
cwb_data = "cwb_weather_data"
if not os.path.exists(cwb_data):
    os.mkdir(cwb_data)

#連接現有氣象 api
import urllib.request
import zipfile 
res ="http://opendata.cwb.gov.tw/opendataapi?dataid=F-D0047-093&authorizationkey=CWB-3FB0188A-5506-41BE-B42A-3785B42C3823"
urllib.request.urlretrieve(res,"F-D0047-093.zip")
f=zipfile.ZipFile('F-D0047-093.zip')