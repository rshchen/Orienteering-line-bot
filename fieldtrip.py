from flask import Flask, request, abort , render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, MessageAction, TextMessage, ImageMessage, TextSendMessage, \
    ImageSendMessage, StickerSendMessage, LocationSendMessage, AudioSendMessage, VideoSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, FollowEvent, URIAction




        

import sqlite3
import re
import json

# import 自己寫的函數
import buttons
import send_func




# 加载 .env 文件
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# 從.env file拿取環境設定
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')


line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


# 團隊成員資料
team_members = [
    {"name": "Alice", "role": "項目經理", "image": "member1.jpeg"},
    {"name": "Bob", "role": "前端工程師", "image": "member2.jpeg"},
    {"name": "Charlie", "role": "後端工程師", "image": "member3.jpeg"},
    {"name": "Daisy", "role": "設計師", "image": "member4.jpeg"},
]

@app.route("/gp_intro", methods=["GET"])
def home():
    return render_template('gp_intro.html', members=team_members)


@app.route("/", methods=["POST"])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: ",body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Token or Secret is wrong.")
        abort(400)
    except LineBotApiError as e:
        app.logger.info("Error-log: " + str(e))
    return 'OK'





@handler.add(MessageEvent)
def handle_message(event):
    # 擷取使用者資料
    UserId = event.source.user_id
    profile = line_bot_api.get_profile(UserId)
    type = event.message.type
    
    # 擷取使用者id的一部分作為新的id，加快搜尋速度
    part_UserId = '%s'%UserId[0:5]

    # connect to the database
    con = sqlite3.connect('fieldtrip_db/fieldtrip.db')

    # 搜尋所有使用者的id
    check = con.execute('SELECT id FROM level').fetchall()
    # 最後一題的題號
    qn_last = con.execute('SELECT qn_nu FROM qa').fetchall()[-1][0]
    

    if ('%s' %part_UserId ,) not in check:
            message = TextSendMessage('我快等不及了！趕快開始遊戲啦！')
        

    else:
        qn_nu = con.execute('SELECT qn_nu FROM level WHERE id = (?)', (part_UserId,)).fetchone()[0]
        qn_read = con.execute('SELECT qn_read FROM level WHERE id = (?)', (part_UserId,)).fetchone()[0]
        suppl_read = con.execute('SELECT suppl_read FROM level WHERE id = (?)', (part_UserId,)).fetchone()[0]
        ans_text_exact = con.execute('SELECT ans_text_exact FROM qa WHERE qn_nu=(?)', (qn_nu, )).fetchone()[0]
        ans_text_con = con.execute('SELECT ans_text_con FROM qa WHERE qn_nu=(?)', (qn_nu, )).fetchone()[0]
        ans_text_multi = con.execute('SELECT ans_text_multi FROM qa WHERE qn_nu=(?)', (qn_nu, )).fetchone()[0]
        ans_img = con.execute('SELECT ans_img FROM qa WHERE qn_nu=(?)', (qn_nu, )).fetchone()[0]
        hint_final = con.execute('SELECT hint_final FROM qa WHERE qn_nu=(?)',(qn_nu,)).fetchone()[0]
        
        if ans_img and type == "image":
                message = [ TextSendMessage('拍得不錯喔！')]+[buttons.suppl()]
                qn_nu += 1
                con.execute('UPDATE level SET qn_nu = (?) WHERE id = (?) ', (qn_nu, part_UserId))
                con.execute('UPDATE level SET suppl_read = 0 WHERE id = (?)', (part_UserId,))
        elif type != 'text':
            message = TextSendMessage('請專心！')
        elif qn_nu == 1:
            text = event.message.text
            match = re.match(ans_text_exact, text)
            if match:
                message = [ TextSendMessage('%s同學，請注意安全，祝你旅途愉快！'%text)]+[buttons.qn()]
                qn_nu += 1
                con.execute('UPDATE level SET qn_read = 0 WHERE id = (?)', (part_UserId,))
                con.execute('UPDATE level SET qn_nu = (?) WHERE id = (?) ', (qn_nu, part_UserId))
            else:
                message = TextSendMessage('同學，輸入格式錯誤，不要挑戰我的智商！')
        elif qn_nu != qn_last:
            text = event.message.text
            if suppl_read == 0 and text != 'Supplement':
                message = TextSendMessage('同學，老師花了這麼多心血，不看補充資料，說不過去吧！')
            elif qn_read == 0 and text != 'Next':
                message = TextSendMessage('同學不要急，先看一下題目吧！')
            elif text == 'Next':
                con.execute('UPDATE level SET qn_read = 1 WHERE id = (?)', (part_UserId,))
                message = send_func.send_qn(qn_nu, con)
            elif text == 'Supplement':
                con.execute('UPDATE level SET suppl_read = 1 WHERE id = (?)', (part_UserId,))
                message = send_func.send_suppl(qn_nu-1, con) + [buttons.qn()]
                con.execute('UPDATE level SET qn_read = 0 WHERE id = (?)', (part_UserId,))

            elif ans_text_exact and text == ans_text_exact:
                message = [buttons.suppl()]
                qn_nu += 1
                con.execute('UPDATE level SET qn_nu = (?) WHERE id = (?) ', (qn_nu, part_UserId))
                con.execute('UPDATE level SET suppl_read = 0 WHERE id = (?)', (part_UserId,))
            elif ans_text_con and (ans_text_con in text):
                message = [buttons.suppl()]
                qn_nu += 1
                con.execute('UPDATE level SET qn_nu = (?) WHERE id = (?) ', (qn_nu, part_UserId))
                con.execute('UPDATE level SET suppl_read = 0 WHERE id = (?)', (part_UserId,))
            elif ans_text_multi and (text in json.loads(ans_text_multi)):
                message = [buttons.suppl()]
                qn_nu += 1
                con.execute('UPDATE level SET qn_nu = (?) WHERE id = (?) ', (qn_nu, part_UserId))
                con.execute('UPDATE level SET suppl_read = 0 WHERE id = (?)', (part_UserId,))

            elif hint_final:
                message = TextSendMessage(hint_final)
            else:
                message = send_func.send_random_hint(qn_nu)


        elif qn_nu == qn_last:
            text = event.message.text
            if suppl_read == 0 and text != 'Supplement':
                message = TextSendMessage('同學，老師花了這麼多心血，不看一下補充資料，說不過去吧！')
            elif qn_read == 0 and text != 'Next':
                message = TextSendMessage('同學不要急，先看一下題目吧！')
            elif text == 'Next':
                con.execute('UPDATE level SET qn_read = 1 WHERE id = (?)', (part_UserId,))
                message = send_func.send_qn(qn_nu, con)
            elif text == 'Supplement':
                con.execute('UPDATE level SET suppl_read = 1 WHERE id = (?)', (part_UserId,))
                message = send_func.send_suppl(qn_nu-1, con) + [buttons.qn()]
                con.execute('UPDATE level SET qn_read = 0 WHERE id = (?)', (part_UserId,))
            elif ans_text_exact == None and ans_text_con == None:
                message = send_func.send_suppl(qn_nu, con)
            elif ans_text_exact and text == ans_text_exact:
                message = send_func.send_suppl(qn_nu, con)
            elif ans_text_con and (ans_text_con in text):
                message = send_func.send_suppl(qn_nu, con)
            elif hint_final:
                message = TextSendMessage(hint_final)
            else:
                message = send_func.send_random_hint(qn_nu)
                
    if type == 'text':
        text = event.message.text
        if text == 'Game introduction':
            message = TextSendMessage('建置中')
        if text == 'Group introduction':
            message = buttons.gp_intro()
        if text == 'Game':
            #delete the data in session.db
            con.execute("DELETE FROM level WHERE id = (?)",(part_UserId,) )
            #insert a new data of this id into the table named level with question number 1
            message =  send_func.send_qn(1, con)
            con.execute("INSERT INTO level (id) values (? )",(part_UserId,) )
            con.execute("UPDATE level SET (qn_nu, qn_read, suppl_read) = (1, 1, 1) WHERE id = (?)",(part_UserId,) )

    con.commit()
    con.close()
    line_bot_api.reply_message(event.reply_token,message)

if __name__ == "__main__":
    app.run()







