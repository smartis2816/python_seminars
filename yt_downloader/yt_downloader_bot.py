import telebot
from pytube import YouTube

token = '5711791663:AAEMJRZt3-pDMCbs4bGb09B0orNwpGb0Fjk'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет ✌️ ')
    bot.send_message(message.chat.id,'Отправь ссылку на ролик в YouTube, который хочешь скачать ')

@bot.message_handler(content_types=['text'])
def choose_video(message):
    global yt
    yt = YouTube(message.text)
    bot.send_message(message.chat.id,f'Название видео - {yt.title}')
    bot.send_message(message.chat.id,'Подожди немного...')
    stream = yt.streams.get_highest_resolution()
    stream.download(filename='Твой видеоролик.mp4')
    video = open('Твой видеоролик.mp4', 'rb')
    bot.send_video(message.chat.id, video=video)
   

print('start')

bot.polling(none_stop=True)