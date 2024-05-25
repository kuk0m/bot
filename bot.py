import telebot
from telebot import types
import random
import time
import random
import os
print(os.path)
token = "7149459351:AAHT2hba2SSTthFjyUW2gjFHogLKX7eDkAA"
bot = telebot.TeleBot(token)
chat_id = 6152371245
banwords=['durak', 'ba']
who1 = ["Весёлый", "Злой", "Крутой"]
who2 = ["Осьменог", "Кот", "Памперс"]
who3 = ["Александр", "Генадий", "Артём"]

coin_flip =["orel", "reshka"]
# print(random.randint(1,10))
# print(random.choice(coin_flip))

@bot.message_handler(commands=["start"])
def hello(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttom1 = types.KeyboardButton("Горы")
    buttom2 = types.KeyboardButton("Лев")
    buttom3 = types.KeyboardButton("Дельфин")
    markup1.add(buttom1, buttom2, buttom3)
    bot.send_message(message.chat.id, f"Hello! {message.from_user.first_name} ",  reply_markup = markup1)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, f"{message.chat.id}cgubenowfimp")

@bot.message_handler(commands=["picture"])
def picture(message):
    img = open(r"C:\Users\Ученик\PycharmProjects\pythonProject1\media\picture.jpg", 'rb')
    bot.send_photo(message.chat.id, img)

@bot.message_handler(commands=["me"])
def text(message):
    markup1 = types.InlineKeyboardMarkup()
    buttom1 = types.InlineKeyboardButton("whatsup", url='https://github.com/kuk0m/bot/blob/main/test.py')
    buttom2 = types.InlineKeyboardButton("жми, жми", url='https://zoo-dom.com/oleni.html')
    markup1.row(buttom1, buttom2)
    bot.send_message(message.chat.id, "me", reply_markup=markup1)


@bot.message_handler(commands=["random"])
def text(message):
    markup1 = types.InlineKeyboardMarkup()
    buttom1 = types.InlineKeyboardButton("orel", callback_data="orel")
    buttom2 = types.InlineKeyboardButton("reshka", callback_data="reshka")
    markup1.row(buttom1, buttom2)
    bot.send_message(message.chat.id, "Орёл и решка", reply_markup=markup1)

@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    cf = (random.choice(coin_flip))
    ppp = open(r"C:\Users\Ученик\PycharmProjects\pythonProject1\media\picture.jpg", 'rb')
    if call.data=='orel':


        bot.send_message(call.message.chat.id, f"Вы выбрали {call.data}")
    if call.data=='reshka':
        bot.send_message(call.message.chat.id, f"Вы выбрали {call.data}")
    bot.send_animation(call.message.chat.id, ppp)

    time.sleep(2)
    bot.send_message(call.message.chat.id, f"Выпал {cf} ")
    if cf == call.data:
        bot.send_message(call.message.chat.id, "Вы выйграли")
    else:
        bot.send_message(call.message.chat.id, "Вы проиграли")
@bot.message_handler(commands=["who"])
def text(message):
    x = (random.choice(who1))
    y = (random.choice(who2))
    z = (random.choice(who3))
    bot.send_message(message.chat.id, bot.send_message(message.chat.id, f"{x} Сегодня вы {x} {y} {z}"))


@bot.message_handler(commands=["clicker"])
def text(message):
    x = 0

    markup = types.InlineKeyboardMarkup()
    buttom = types.InlineKeyboardButton("click", callback_data="1")
    markup.row(buttom)
    bot.send_message(message.chat.id,f"{x}",reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == '1':
        x = x + 1
        bot.send_message(message.chat.id, f"{x}")

@bot.message_handler(commands=["game"])
def text(message):
    print(message)
    bot.send_message(message.chat.id, f" В этой игре я загадываю число от 1 до 100, и вы угадываете, а я говорю: больше или меньше")


@bot.message_handler(func=lambda me0ssage:True)
def text(message):
    x = random.randint(1, 100)
    try:
        print(x)
        y = int(message.text)
        if y == x:
            bot.send_message(message.chat.id, "Вы угадали!")
        elif y >= x:
            bot.send_message(message.chat.id, "меньше")
        elif y <= x:
            bot.send_message(message.chat.id, "больше")
    except ValueError:
        bot.send_message(message.chat.id, "Введите число")
    # y = int(user_message.text)
    # bot.send_message(message.chat.id, f" OK")
    # x = int(random.randint(0, 100))
    #
    # if y == x:
    #     bot.send_message(message.chat.id,"Вы угадали!")
    # elif y >= x:
    #     bot.send_message(message.chat.id, "меньше")
    # elif y <= x:
    #     bot.send_message(message.chat.id, "больше"

# @bot.message_handler(chat_id=[chat_id], commands=['update'])
# def update_command(message):






@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.lower() == "горы":
        img = open("media/Горы.jpg", 'rb')
        bot.send_photo(message.chat.id, img)
    elif message.text.lower() == "лев":
        img = open("media/Лев.jpg", 'rb')
        bot.send_photo(message.chat.id, img)
    elif message.text.lower() == "дельфин":
        imp = open("media/дельфин.jpg", 'rb')
        bot.send_photo(message.chat.id, imp)

    elif message.text in banwords:
        bot.ban_chat_member(message.chat.id, message.from_user.id)
        bot.send_message(message.chat.id, "выгнан")



# @bot.message_handler(chat_id=[-4151645209], commands=['update'])
# def update_command(message):
#     bot.set_my_commands(
#     commands=[telebot.types.BotCommand('start', 'Начало работы'),
#               telebot.types.BotCommand('game', 'Игра с числами'),
#               telebot.types.BotCommand('random', 'Орёл или решка'),
#               telebot.types.BotCommand('who', 'кто ты по сегодня'),
#               telebot.types.BotCommand('me', 'Информация обо мне'),
#               telebot.types.BotCommand('picture', 'Картинка')
#               ],
#                     scope=telebot.types.BotCommandScopeChat(-4151645209))
bot.polling(non_stop=True)
