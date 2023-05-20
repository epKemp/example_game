import telebot
import random

API_TOKEN = '5828710438:AAFyq4PK9X11PbgDCK3udaYgWj4oX2yW58Q'

my_bot = telebot.TeleBot(API_TOKEN)

@my_bot.message_handler(commands=['start'])


def send_welcome(message):
    mes = 'Привет, я бот. если хочешь поиграть в "камень-ножницы-бумага" - пиши "играть", если хочешь поугадывать случайное число от 0 до 10 - пиши "угадать'
    my_bot.send_message(message.chat.id, mes)



@my_bot.message_handler(content_types=['text'])


def send_te_text(message):
    #print(message)
    tmp = message.text.lower()
    list_mes = tmp.split()
    list = ['привет', 'погод', 'угадать', 'камень', 'ножницы', 'бумага','1','2','3','4','5','6','7','8','9','10']
    l1 = [1, 2, 3]  # 1 - ножницы 2 - бумага 3 - камень
    l2 = [1 , 2, 3, 4, 5, 6, 7 ,8, 9, 10]
    r = random.choice(l2)
    ch = message.text.lower()
    mes1 = (r, 'ты угадал')
    mes2 = (r, 'не угадал')
    if tmp in list:
        pass
    for word in list_mes:
        #print(word)
        if 'погод' in word:
            mes = 'тепло'
            my_bot.send_message(message.chat.id, mes)
            break
        break
    for word in list_mes:
        print(word)
        if 'играть' in word:
            mes = 'давай поиграем'
            my_bot.send_message(message.chat.id, mes)
            break
        b = random.choice(l1)
        i = message.text.lower()
        if i == 'ножницы' and b == 1:
            my_bot.send_message(message.chat.id, 'ножницы. ничья')
            break
        if i == 'ножницы' and b == 2:
            my_bot.send_message(message.chat.id, 'бумага. я проиграл')
            break
        if i == 'ножницы' and b == 3:
            my_bot.send_message(message.chat.id, 'камень. я победил')
            break
        if i == 'бумага' and b == 1:
            my_bot.send_message(message.chat.id, 'ножницы. я победил')
            break
        if i == 'бумага' and b == 2:
            my_bot.send_message(message.chat.id, 'бумага. ничья')
            break
        if i == 'бумага' and b == 3:
            my_bot.send_message(message.chat.id, 'камень. я проиграл')
            break
        if i == 'камень' and b == 1:
            my_bot.send_message(message.chat.id, 'ножницы. я проиграл')
            break
        if i == 'камень' and b == 2:
            my_bot.send_message(message.chat.id, 'бумага. я победил')
            break
        if i == 'камень' and b == 3:
            my_bot.send_message(message.chat.id, 'камень. ничья')
            break
        break
    for word in list_mes:
        #print(word)
        if 'привет' in word:
            mes = 'ку'
            my_bot.send_message(message.chat.id, mes)
            break
        break
    for word in list_mes:
        if 'угадать' in word:
            mes3 = 'загадай число от 1 до 10 и напиши его мне'
            my_bot.send_message(message.chat.id, mes3)
            break

        if r == tmp:
            my_bot.send_message(message.chat.id, mes1)
            break
        elif tmp :
            my_bot.send_message(message.chat.id, mes2)
            break
        break

    else:
        my_bot.send_message(message.chat.id, "я тебя не понимаю")


my_bot.infinity_polling()