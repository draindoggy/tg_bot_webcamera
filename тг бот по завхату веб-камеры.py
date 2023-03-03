import telebot
import os
bot = telebot.TeleBot('токен')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='привет, {0.first_name}!, сейчас ты получишь доступ к своей веб-камере прямо из телеграма!')
@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'запусти камеру':
        os.startfile(r'C:\Users\motor\OneDrive\Рабочий стол\pythonProject1\dist\webcamera.exe')
        bot.send_message(message.from_user.id, text='камера запущена, наслаждайтесь видом!')
bot.infinity_polling()

