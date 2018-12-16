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
#import urllib3
#from bs4 import BeautifulSoup
#from urllib.request import urlretrieve
import random


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



def chat(event_message):   
    User_Msg = ['嗨','你好','歡迎!','你好','嗨，最近如何?','你好嗎?','很高興見到你','你還好嗎?','怎麼了?','早上好，你好嗎?','我挺好的，你呢','我也還不錯','那很好','是啊','你好','你好','你好嗎?','我還不錯','那很好','是啊','有需要幫忙嗎?']    
    Respond_Msg = ['你好','你好,很高興為你服務','吃飯了嗎?','嗨，最近如何?','最近失眠了 你呢?','還不錯，你呢?','很高興見到你','我很好，你呢?','早ㄤ!','早上好，你好嗎?','我挺好的，你呢','我也還不錯','那很好','是啊','你好','你好','你好嗎?','我還不錯','那很好','是啊','有需要幫忙嗎?']
    Greet_User_Msg = ['你好','嗨','歡迎!','你好','嗨，最近如何?','你好嗎?','很高興見到你','你還好嗎?','怎麼了?']
    Greet_Respond_Msg = ['你好,很高興為你服務','吃飯了嗎?','嗨，最近如何?','最近失眠了 你呢?','還不錯，你呢?','很高興見到你','我很好，你呢?','早ㄤ!',]
    Conversation_User_Msg = ['早上好，你好嗎?','我挺好的，你呢','我也還不錯','那很好','是啊','你好','你好','你好嗎?','我還不錯','那很好','是啊','有需要幫忙嗎?']
    Conversation_Respond_Msg = []
    
    count = 0    
    text = text = random.choice(Respond_Msg)
    msg = TextSendMessage(text)
    Respond_Msg.append(event_message)
    #for Msg in User_Msg :
    #   if event_message != Msg:
    #        msg = TextSendMessage(event_message)
    #        User_Msg.append(event_message)
    #        Respond_Msg.append(event_message)
    #        break
    #    else :           
    #        while count <= len(User_Msg):
    #            if User_Msg[count] == event_message and count < len(User_Msg):               
    #                count += 1
    #                text = Respond_Msg[count]
    #                msg = TextSendMessage(text)
    #                break     
    #           count += 1
    #       break
    
   
    return msg
        
    
    
#for Msg in User_Msg :
 #       if event_message != Msg:
  #          msg = TextSendMessage(event_message)
   #         User_Msg.append(event_message)
    #        Respond_Msg.append(event_message)
     #   else :           
      #      text = random.choice(Respond_Msg)
       #     msg = TextSendMessage(text)

    #if event_message == "嗨": 
    #    text = random.choice ( ['嗨', '你好', '最近好嗎?', '你好嗎?', '很高興見到你'] )
    #    msg = TextSendMessage(text)
     
    
    #text = random.choice ( ['嗨', '你好', '最近好嗎?', '你好嗎?', '很高興見到你','你再問我嗎?','最近失眠了 你呢?'] )
    #msg = TextSendMessage(text)
    
        
    


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
                            URITemplateAction(
                                label='研究所',
                                uri='http://www.cs.nptu.edu.tw/files/11-1092-3154.php?Lang=zh-tw'
                            )                            
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
                            URITemplateAction(
                                label='大學部',
                                uri='http://www.cs.nptu.edu.tw/files/11-1092-3164.php?Lang=zh-tw'
                            ),
                            URITemplateAction(
                                label='未來學生',
                                uri='http://www.cs.nptu.edu.tw/files/11-1092-3182.php?Lang=zh-tw'
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
            URITemplateAction(
                label='未來發展',
                uri='http://www.cs.nptu.edu.tw/files/11-1092-7952-1.php?Lang=zh-tw'
            )            
        ]
    )
)
    return message






def teacher():
    message = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackTemplateAction(
                    label='楊政興 主任',
                    text='楊政興 主任',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackTemplateAction(
                    label='王朱福 教授',
                    text='王朱福 教授',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackTemplateAction(
                    label='施釗德 教授',
                    text='施釗德 教授',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackTemplateAction(
                    label='蔡進聰 教授',
                    text='蔡進聰 教授',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackTemplateAction(
                    label='黃樹乾 副教授',
                    text='黃樹乾 副教授',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackTemplateAction(
                    label='鄭經文 副教授',
                    text='鄭經文 副教授',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item2.jpg',
                action=PostbackTemplateAction(
                    label='助理教授',
                    text='助理教授',
                    data='action=buy&itemid=2'
                )
            )
        ]
    )
    )
    return message



def teacher2():
    message = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackTemplateAction(
                    label='林志隆 助理教授',
                    text='林志隆 助理教授',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackTemplateAction(
                    label='林彥廷 助理教授',
                    text='林彥廷 助理教授',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackTemplateAction(
                    label='翁麒耀 助理教授',
                    text='翁麒耀 助理教授',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item2.jpg',
                action=PostbackTemplateAction(
                    label='黃奕欽 助理教授',
                    text='黃奕欽 助理教授',
                    data='action=buy&itemid=2'
                )
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
        message = teacher()
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == "助理教授": 
        message = teacher2()
        line_bot_api.reply_message(event.reply_token, message)   
    if event.message.text == "實驗室": 
        message = TemplateSendMessage(
        alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://example.com/image.jpg',
                title='實驗室',
                text='實驗室、教學及討論空間',
                actions=[
                    URITemplateAction(
                        label='民生校區五育樓B1',
                        uri='http://www.cs.nptu.edu.tw/files/11-1092-7948-1.php?Lang=zh-tw'
                    ),
                    URITemplateAction(
                        label='民生校區教學科技館4樓',
                        uri='http://www.cs.nptu.edu.tw/files/11-1092-7949-1.php?Lang=zh-tw'
                    ),
                    URITemplateAction(
                        label='民生校區教學科技館5樓',
                        uri='http://www.cs.nptu.edu.tw/files/11-1092-8005-1.php?Lang=zh-tw'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)    


    if event.message.text == "系所介紹": 
        message = TextSendMessage(text='在政府持續推動數位化台灣，以及資訊相關產業的蓬勃發展之下，在可預見的未來，資訊人才仍是就業市場的最大需求之一。屏東師院為發展成為綜合型大學，並考慮就業市場的需求，特成立本系，以培育資訊科技研發與應用人才。')
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == "發展特色": 
        message = TextSendMessage(text='本系致力於智慧雲端系統與應用開發之研發工作。')       
        line_bot_api.reply_message(event.reply_token, message)        
       
  
    if event.message.text == "發票": 
        message = TextSendMessage(text='https://www.etax.nat.gov.tw/etw-main/web/ETW183W1/')
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text == "天氣": 
        message = TextSendMessage(text='https://www.cwb.gov.tw/V7/forecast/')
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == "幣值": 
        message = TextSendMessage(text='https://zt.coinmill.com/')
        line_bot_api.reply_message(event.reply_token, message)
    
    
    if event.message.text == '你愛我嗎?':
        message = TextSendMessage(text='我對你的感情，是人類和bot之間獨有的信任和友誼 你可以把它叫做愛。')
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
        message = chat(event.message.text)
        #message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token, message)

    

    


    

    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)




