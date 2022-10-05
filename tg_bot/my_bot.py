import telebot
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
import os
import time

botToken = '5706346479:AAGeJwOZe73cfpsPfyAZnVvBbVE-RepRyp4'
bot = telebot.TeleBot(botToken, parse_mode=None)

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('95acb5f736fbc43ac2a1ffe26ee76c54', config_dict)

# place = input("Укажите город/страну: ")

# mgr = owm.weather_manager()
# observation = mgr.weather_at_place(place)
# w = observation.weather
# print(w)

@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text.lower() == "/start" or message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Напишите название города." + "\n")
    else:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place('Moscow')
        weather = observation.weather
        temp = weather.get_temperature("celsius")["temp"]
        print(time.ctime(), "User id:", message.from_user.id)
        print(time.ctime(), "Message:", message.text.title(), temp, "C", weather.get_detailed_status())
        answer = "В городе " + message.text.title() + " сейчас " + weather.get_detailed_status() + "." + "\n"
        answer += "Температура около: " + str(temp) + " С" + "\n\n"
        if temp < -10:
            answer += "Пи**ц как холодно, одевайся как танк!"
        elif temp < 10:
            answer += "Холодно, одевайся теплее."
        elif temp > 25:
            answer += "Жарень."
        else:
            answer += "На улице вроде норм!!!"

        bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)
