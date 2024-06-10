from linebot.models import  TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, URIAction


# 加载 .env 文件
import os
from dotenv import load_dotenv
load_dotenv()
# 從.env file拿取環境設定
gp_intro_uri = os.getenv('gp_intro_uri')


# 設定按鈕樣版
def suppl():
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            title='恭喜答對！',
            text= '請查看補充資料',
            actions=[
                MessageTemplateAction(
                    label='知識充電站',
                    text='Supplement',
                )
            ]
        )
    )
    return message
 
def qn():
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            title='恭喜過關！',
            text= '請前往下一題',
            actions=[
                MessageTemplateAction(
                    label='下一題',
                    text='Next',
                )
            ]
        )
    )
    return message

def gp_intro():
    message = TemplateSendMessage(
        alt_text='團隊介紹',
        template=ButtonsTemplate(
            title='團隊介紹', text='點擊以下按鈕以查看我們的網站',
            actions=[
                URIAction(
                    label='訪問我們的網站',
                    uri = gp_intro_uri
                )
            ]
        )
    )
    return message
