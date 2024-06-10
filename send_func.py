from linebot import LineBotApi
from linebot.models import ImageSendMessage, TextSendMessage


import random


# send question and following hint
def send_qn(qn_nu, con):
    qn_type = con.execute('SELECT * FROM qa WHERE qn_nu = 0').fetchone()
    qn_inf = con.execute('SELECT * FROM qa WHERE qn_nu = (?)', (qn_nu, )).fetchone()
    message = []
    for i in range(1,5):
        if qn_inf[i] != None:
            match qn_type[i]:
                case '1':
                    message += [TextSendMessage(qn_inf[i])]
                case '3':
                    message += [ImageSendMessage(qn_inf[i], qn_inf[i])]
    return message
    
# send supplement
def send_suppl(qn_nu, con):
    qn_type = con.execute('SELECT * FROM qa WHERE qn_nu = 0').fetchone()
    qn_inf = con.execute('SELECT * FROM qa WHERE qn_nu=(?)',(qn_nu,)).fetchone()
    message = []
    for i in range(10,12):
        if qn_inf[i] != None:
            match qn_type[i]:
                case '1':
                    message += [TextSendMessage(qn_inf[i])]
                case '3':
                    message += [ImageSendMessage(qn_inf[i], qn_inf[i])]
    return message
    
def send_random_hint(qn_nu):
    hint_nu = random.randint(1, 5)
    match hint_nu:
        case 1:
            message = TextSendMessage('答錯了！不要亂猜！')
        case 2:
            message = TextSendMessage('加油好嗎？')
        case 3:
            message = TextSendMessage('這題能答錯也是不簡單')
        case 4:
            message = TextSendMessage('不對唷')
        case 5:
            message = TextSendMessage('不是吧！？')
    return message

