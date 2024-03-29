import telebot
from telebot import types
import random
token = "7149459351:AAHT2hba2SSTthFjyUW2gjFHogLKX7eDkAA"
bot = telebot.TeleBot(token)
banwords=['durak', 'ba']

# coin_flip =["Орёл", "Решка"]
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
    bot.send_message(message.chat.id, "cgubenowfimp")

@bot.message_handler(commands=["picture"])
def picture(message):
    img = open("media/picture.jpg", 'rb')
    bot.send_photo(message.chat.id, img)

@bot.message_handler(commands=["me"])
def text(message):
    markup1 = types.InlineKeyboardMarkup()
    buttom1 = types.InlineKeyboardButton("whatsup", url='https://github.com/kuk0m/bot/blob/main/test.py')
    buttom2 = types.InlineKeyboardButton("gjhfk", url='https://zoo-dom.com/oleni.html')
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
    if call.data=='orel':
        bot.send_message(call.message.chat.id, f"Вы выбрали {call.data}")


@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.lower() == "горы":
        img = open("media/Горы.jpg", 'rb')
        bot.send_photo(message.chat.id, img)
    elif message.text.lower() == "лев":
        img = open("media/лев.jpg", 'rb')
        bot.send_photo(message.chat.id, img)
    elif message.text.lower() == "дельфин":
        imp = open("media/дельфин.jpg", 'rb')
        bot.send_photo(message.chat.id, imp)

    elif message.text in banwords:
        bot.ban_chat_member(message.chat.id, message.from_user.id)
        bot.send_message(message.chat.id, "выгнан")


bot.polling(non_stop=True)
