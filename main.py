
import os
from pytube import YouTube
from telebot import TeleBot,telebot,types

bot = telebot.TeleBot('5118039174:AAE6E83OIk_kSsZlnbTs-yEZ05QkrqNEMG8')


@bot.message_handler(commands=['start'])
def welcome_message(msg):
    bot.send_message(msg.chat.id,'Send valid youtube link')
    
    
@bot.message_handler(func = lambda m:True)
def audio_download(msg):
    yt = YouTube(msg.text)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download('/storage/emulated/0/A')
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print('Downloading...')
    with open(new_file,'rb') as e:
        bot.send_audio(msg.chat.id,e,msg.message_id)

bot.infinity_polling()
