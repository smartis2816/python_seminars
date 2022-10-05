# import telebot
# from pyowm.owm import OWM
# from pyowm.utils.config import get_default_config
# import os
# import time

# botToken = '5706346479:AAGeJwOZe73cfpsPfyAZnVvBbVE-RepRyp4'
# bot = telebot.TeleBot(botToken, parse_mode=None)

# config_dict = get_default_config()
# config_dict['language'] = 'ru'
# owm = OWM('95acb5f736fbc43ac2a1ffe26ee76c54', config_dict)

# # place = input("Укажите город/страну: ")

# # mgr = owm.weather_manager()
# # observation = mgr.weather_at_place(place)
# # w = observation.weather
# # print(w)

# @bot.message_handler(content_types=['text'])
# def send_message(message):


# bot.polling(none_stop=True)
