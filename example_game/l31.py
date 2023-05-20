import telebot
import random
from telebot import types
import requests
from bs4 import BeautifulSoup

# response = requests.get('https://store.steampowered.com/specials/')
# with open('index.html', 'w') as file:
#     file.write(response.text)
def get_game():
    with open ('index.html', 'r') as file:
        sp = BeautifulSoup(file,'lxml')
        name = sp.find('div', class_='apphub_AppName').text
        print(name)
        return name



API_TOKEN = '5828710438:AAFyq4PK9X11PbgDCK3udaYgWj4oX2yW58Q'

my_bot = telebot.TeleBot(API_TOKEN)
a1 = "Заходишь в Google с нового компа и реклама такая растерянная: скидки на духи? может, отдых в Голландии? тренинг надо какой? не молчи же!"""
a2 = """Учитель: Кто может привести примеры того, что искусственный интеллект легко заменит навсегда?
# Я: *поднимаю руку*
# Учитель: Молодец, Иванов. Ребята, а какие ещё будут примеры, кроме Иванова?"""
an = [a1, a2]
z1 = """Кто любить не устает,
Пироги для нас печет,
Вкусные оладушки?
Это наша..."""
z2 = """Я у мамы не один,
У неё ещё есть сын,
Рядом с ним я маловат,
Для меня он — старший..."""
z3 = """Заплелись густые травы,
Закудрявились луга,
Да и сам я весь кудрявый,
Даже завитком рога."""
z4 = """У него огромный рот,
Он зовется …"""
zagadki = [z1, z2, z3, z4]
anek = random.choice(an)

@my_bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.text == '/help':
        mes = "команды: /button, /links, /functions "
        my_bot.send_message(message.chat.id, mes)
    else:
        mes = """#привет, команды для управленя\n /button, /links, /help , /functions"""
        my_bot.send_message(message.chat.id, mes)


@my_bot.message_handler(commands=['button'])
def show_button(message):
     marcup = types.ReplyKeyboardMarkup(row_width=1)
     btn_1 = types.KeyboardButton("/links ")
     btn_2 = types.KeyboardButton("/functions ")
     btn_3 = types.KeyboardButton("/help ")
     btn_4 = types.KeyboardButton("/games ")
     marcup.add(btn_1, btn_2, btn_3, btn_4)
     my_bot.send_message(message.chat.id, 'вот доступные кнопки', reply_markup=marcup)


@my_bot.message_handler(commands=['text'])
def send_te_text(message):
     a = message.text.lower()
     if a == "links ":
        my_bot.send_message(message.chat.id, 'вы нажали на button 1')
     elif message.text == "button 2 ":
        my_bot.send_message(message.chat.id, 'вы нажали на button 2')
     elif message.text == "button 3 ":
         my_bot.send_message(message.chat.id, 'вы нажали на button 3')
     elif message.text == "/games ":
         game_name = get_game()
         mes = f"Name: {game_name}"
         my_bot.send_message(message.chat.id, mes)


@my_bot.message_handler(commands=['links'])
def send_link(message):
     marcup = types.InlineKeyboardMarkup()
     btn1 = types.InlineKeyboardButton('python', url='https://www.python.org/')
     btn2 = types.InlineKeyboardButton('steam', url='https://store.steampowered.com/')
     marcup.add(btn1, btn2, row_width=1)
     my_bot.send_message(message.chat.id, 'ссылки:', reply_markup=marcup)


@my_bot.message_handler(commands=['functions'])
def send_da(message):
     marcup = types.InlineKeyboardMarkup()
     btn1 = types.InlineKeyboardButton('анекдот', callback_data='anek')
     btn2 = types.InlineKeyboardButton('загадки', callback_data='zagad')
     marcup.add(btn1, btn2, row_width=1)
     my_bot.send_message(message.chat.id, 'функции:', reply_markup=marcup)


@my_bot.callback_query_handler(func=lambda call:True)
def callback(call):
     if call.message:
         if call.data == 'anek':
             anek = random.choice(an)
             my_bot.send_message(call.message.chat.id, anek)
         if call.data == 'zagad':
             zag = random.choice(zagadki)
             my_bot.send_message(call.message.chat.id, zag)
             if zag == z1:
                     my_bot.send_message(call.message.chat.id, f"||бабушка||", parse_mode='MarkdownV2')
             if zag == z2:
                     my_bot.send_message(call.message.chat.id, f"||брат||", parse_mode='MarkdownV2')
             if zag == z3:
                     my_bot.send_message(call.message.chat.id, f"||баран||", parse_mode='MarkdownV2')
             if zag == z4:
                     my_bot.send_message(call.message.chat.id, f"||бегемот||", parse_mode='MarkdownV2')



my_bot.infinity_polling()
