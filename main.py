
import os
import youtube_dl
from telebot import TeleBot,telebot,types
from telebot.util import user_link
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton

token = "5118039174:AAExJPN34Qlkj-VvPg9NkFrIbwHFKAoPpBQ"
bot = telebot.TeleBot(token,parse_mode="HTML")


markup = InlineKeyboardMarkup()
b1 = InlineKeyboardButton('🦧Official Channel🦧',url='t.me/DevelopersPage')
b2 = InlineKeyboardButton('🦅Official Group🦅',url='t.me/DevelopersChat')
markup.add(b1,b2)

@bot.message_handler(commands=['start'])
def welcome_msg(message):
    user = message.from_user
    bot.reply_to(message,f'Hello dear {user_link(user)} welcome to youtube audio downloader bot\n just send valid youtube link',reply_markup = markup)
  
    
@bot.message_handler(func = lambda m:True)
def audio_download(msg):
    try:
        link = msg.text
        downloader = youtube_dl.YoutubeDL().extract_info(url = link,download=False)
        filename = f"{downloader['title']}.mp3"
        options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([downloader['webpage_url']])
        with open(filename,"rb")as audio:
            bot.send_audio(msg.chat.id,audio,caption=f"{downloader['title']}")
            bot.send_chat_action(msg.chat.id,action="upload_document")
            os.remove(filename)
    except Exception as e:
        print(e)
    
bot.infinity_polling()

