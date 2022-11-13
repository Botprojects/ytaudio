
import os
import pafy
from telebot import TeleBot,telebot,types
from telebot.util import user_link

bot = telebot.TeleBot("5118039174:AAEbw77oG5lXpZJo1Wyl-mbXSiy8iB0Zzlc")


@bot.message_handler(commands=['start'])
def welcome_message(msg):
    bot.send_message(msg.chat.id,f"Hello {user_link(msg.from_user)}Send valid youtube vidoe link")
    
    
@bot.message_handler(func = lambda m:True)
def audio_download(msg):
    downloader = pafy.new(msg.text)
    audio = downloader.audiostreams[0]
    fileName = f"{downloader.title}.mp3"
    audio.download(fileName)
    with open(file,"rb") as audio:
        bot.send_audio(msg.chat.id,e,msg.message_id,caption="f{downloader.title}")

bot.infinity_polling()
