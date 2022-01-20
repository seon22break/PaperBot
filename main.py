from url import *
from parser import *
import telebot
import os
from dotenv import load_dotenv
from config import *
load_dotenv()

bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))
url = Url()
parser = Parser()
allowed_commands = ["/start","/help"]


def listener(message):

    for m in message:
        chat_id = m.chat.id
        texto = m.text

        if texto in allowed_commands:
            return True

        if texto == "holita":
            bot.send_message(chat_id,"patatita")

        processUrl = url.getRequestPage(texto)

        if not processUrl:
            bot.send_message(chat_id,URL_ERROR)
            return True
        
        if not parser.setContentPage(processUrl):
            bot.send_message(chat_id,CONTENT_ERROR)
            return True

        body = parser.getBodyArticle(url.domain)

        if len(body) > 4095:
            bot.send_message(chat_id,"*"+str(parser.getTitlePage())+"*",parse_mode = "Markdown")
            for x in range(0, len(body), 4095):
                bot.send_message(chat_id,text=body[x:x+4095])
        else:
            bot.send_message(chat_id,CONTENT_ERROR)


                
bot.set_update_listener(listener)


@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.send_message(message.chat.id,WELCOME)


@bot.message_handler(commands=['help'])
def send_welcome(message):
        bot.send_message(message.chat.id,HELP,parse_mode = "Markdown")


bot.polling()


