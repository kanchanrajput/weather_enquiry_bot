#kanchan_weather_inquiry_bot
import telebot
import requests as req
import json

my_weather_bot = telebot.TeleBot("1206342928:AAEpfojM1Aosi3Ks9ShRZAMpkBkUwKYftgk")

@my_weather_bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
    
    my_weather_bot.reply_to(message,"Welcome, This is weather inquiry bot,plz enter the city name for weather inquiry")
    print("message from:" + message.from_user.first_name)

@my_weather_bot.message_handler(func=lambda m: True)

def echo_all(msg):

    city = msg.text

    try:
    
        response = req.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3863ac39fc7b19ea442bbc9dfecd3ed3")

        response_text = json.loads(response.text)
        my_weather_bot.reply_to(msg,"weather report is :"+str(response_text))

    except Exception as e:
        my_weather_bot.reply_to(msg,"some error occured")
        print(e)

my_weather_bot.polling()    
