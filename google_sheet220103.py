
 -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第三章 互動回傳功能
推播push_message與回覆reply_message
"""

###Google sheet
import gspread

gc = gspread.service_account(filename = "mzbot123001.json")
sheet = gc.open_by_key("15g-2coTEOJ5NzERQHg6N-8fKyHnUGo-g2cxX-xyTPv8")
worksheet = sheet.worksheet("mz")
###Google sheet


#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('COe9IVtYYXNq4gvq1UAkylEeLHRaqNqYjna2zwbi4CQ8QFNa6Wn3M/fhwp83As7qxc1bXI6sNX3HtW9tMMkWy5tf24Qs1XklAQvJAx5f3WkwKlXr2EB9eMWnVpPP3h/FpIDfN74sPCqfkAt2aDdquwdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('6d54d7a4820257f64dcd3951ec10f231')

line_bot_api.push_message('U9a0bac79590e0aff662b3c77194f72da', TextSendMessage(text='你可以開始了12152'))

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

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('告訴我秘密',message):

        location_message = LocationSendMessage(
            title='日治時期的古蹟',
            address='總統府',
            latitude=25.040213810016002,
            longitude=121.51238385108306
        )
        line_bot_api.reply_message(event.reply_token, location_message)

        ### Google sheet ####

        val = worksheet.acell('B7').value
        worksheet.update_cell(1,1, "Hello world888999993")
        worksheet.update_cell(1,2, str(val))
        worksheet.update_cell(1,3, val)

        ### Google sheet finish ###

        line_bot_api.reply_message(event.reply_token, TextSendMessage('才不告訴你哩！'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)









#worksheet.batch_clear(["A1:B1"])
