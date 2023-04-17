import telebot
import random
from telebot import types
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pay
import config
config.init()
bot = telebot.TeleBot(config.token, threaded=False)
phone_n = ''
remove_keyboard = types.ReplyKeyboardRemove()
#bot.delete_webhook()

@bot.message_handler(content_types=['sticker'])
def message_r(message):
    st = random.randint(0, 5)
    bot.send_sticker(message.chat.id, config.stickers[st])


@bot.message_handler(commands=['support'])
def help(message):
    bot.send_message(message.chat.id, 'По вопросам сюда -----> https://t.me/iamlolli')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEH8Fdj_joRe30O3i6xML6EdMiAcVoEBgACxgEAAhZCawpKI9T0ydt5Ry4E')

@bot.message_handler(commands=['register'])
def send_welcome(message):
    # запрашиваем у пользователя номер телефона
    phone_n = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    phone_n.add(telebot.types.KeyboardButton('Отправить номер телефона', request_contact=True))
    bot.send_message(message.chat.id, "Привет! Нам нужен твой номер телефона", reply_markup=phone_n)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    global phone_n  # объявляем переменную user_phone как глобальную
    phone_n = message.contact.phone_number[2:]
    bot.send_message(message.chat.id, f"Спасибо, мы сохранили твой номер телефона: {phone_n}")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'Здесь вы можете приобрести ключ {phone_n}')

@bot.message_handler(commands = ['buy'])
def buy(message):
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    atom = types.KeyboardButton('Atomic heart (vk play) - 2499.96Р')
    cyb = types.KeyboardButton('Cyberpunk 2077 (steam) - 3644.97Р')
    call = types.KeyboardButton('Call of Duty: black ops (battle.net) - 449.95Р')
    r6 = types.KeyboardButton('Rainbow six siege(ubisoft) - 1449.96Р')
    mark.add(atom, cyb, call, r6)
    bot.send_message(message.chat.id, 'Выберете игру!', reply_markup=mark)
с = types.KeyboardButton('Я оплатил!')
@bot.message_handler(content_types=['text'])
def message_reply(message):
    global price
    price = ''
    if message.text == 'Atomic heart (vk play) - 2499.96Р':
        price = '2499,96'
        if phone_n == '':
            bot.send_message(message.chat.id, 'Оставте свой номер телефона что мы сделали вам форму оплаты. Это можно сделать по /register')
        else:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.row(с)
            pay.pay(phone_n, price)
            bot.send_message(message.chat.id, 'Мы отправили вам запрос на оплату. Оплатите в ЛК Тинькофф', reply_markup=keyboard)



    if message.text=='Cyberpunk 2077 (steam) - 3644.97Р':
        price = '3644,97'
        if phone_n == '':
            bot.send_message(message.chat.id,
                             'Оставте свой номер телефона что мы сделали вам форму оплаты. Это можно сделать по /register')
        else:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.row(с)
            pay.pay(phone_n, price)
            bot.send_message(message.chat.id, 'Мы отправили вам запрос на оплату. Оплатите в ЛК Тинькофф',
                             reply_markup=keyboard)


    if message.text=='Call of Duty: black ops (battle.net) - 449.95Р':
        price = '449,95'
        if phone_n == '':
            bot.send_message(message.chat.id,
                             'Оставте свой номер телефона что мы сделали вам форму оплаты. Это можно сделать по /register')
        else:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.row(с)
            pay.pay(phone_n, price)
            bot.send_message(message.chat.id, 'Мы отправили вам запрос на оплату. Оплатите в ЛК Тинькофф',
                             reply_markup=keyboard)


    if message.text=='Rainbow six siege(ubisoft) - 1449.96Р':
        price = '1449,96'
        if phone_n == '':
            bot.send_message(message.chat.id,
                             'Оставте свой номер телефона что мы сделали вам форму оплаты. Это можно сделать по /register')
        else:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.row(с)
            pay.pay(phone_n, price)
            bot.send_message(message.chat.id, 'Мы отправили вам запрос на оплату. Оплатите в ЛК Тинькофф',
                             reply_markup=keyboard)


    if message.text == 'ТЕСТ':
        price = '9,96'
        if phone_n == '':
            bot.send_message(message.chat.id,
                             'Оставте свой номер телефона что мы сделали вам форму оплаты. Это можно сделать по /register')
        else:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.row(с)
            pay.pay(phone_n, price)
            bot.send_message(message.chat.id, 'Мы отправили вам запрос на оплату. Оплатите в ЛК Тинькофф',
                             reply_markup=keyboard)


    if message.text == 'Я оплатил!':
        bot.send_message(message.chat.id, 'Сейчас проверю вашу оплату', reply_markup=remove_keyboard)
        pay.pay_conf(price)
        if pay.c == True:
            f = open('file.txt', 'r')
            text = [str(i) for i in f]
            text = [line.rstrip() for line in text]
            words = text
            myArray = words[0]
            words.pop(0)
            with open('file.txt', 'w+') as f:
                f.write("\n".join(text))
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEH8Ftj_jp5GKqXW1890jpwk3u1p5PZ8gACqAEAAhZCawohiU75GjuW2i4E')
            bot.send_message(message.chat.id, f'Спасибо за покупку! Ключ:{myArray}')
        else:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.row(с)
            bot.send_message(message.chat.id, 'Оплата не подтверждена, убедитесь, что вы оплатили', reply_markup=keyboard)
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEIncFkPUNQhBXv18ZvPkhR10sWUZFjgAACsQEAAhZCawr8SvSXguuQMS8E')

bot.polling(none_stop=True)