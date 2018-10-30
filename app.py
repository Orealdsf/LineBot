from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 推送訊息
    line_bot_api.push_message('Ubc4902b9b76350b957769c5376e7f43c',TextSendMessage(text='我是基德 是名機器人'))

    # 回應訊息
    if event.message.text== '圖片' :
        message = ImageSendMessage(
        original_content_url='',
        preview_image_url=''
        )
        line_bot_api.reply_message(event.reply_token, message)
    

    elif event.message.text == '==':
        message = TextSendMessage(text='終於有人知道= =中間不要加空格')
        line_bot_api.reply_message(event.reply_token,message)
    
    else:
        message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token, message)


    

    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
