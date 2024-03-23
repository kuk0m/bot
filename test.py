import telebot
from telebot import types
token = "7149459351:AAHT2hba2SSTthFjyUW2gjFHogLKX7eDkAA"
bot = telebot.TeleBot(token)
banwords=['durak', 'ba']

@bot.message_handler(commands=["start"])
def hello(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttom1 = types.KeyboardButton("hi")
    buttom2 = types.KeyboardButton("huifa")
    buttom3 = types.KeyboardButton("bhfj")
    markup1.add(buttom1, buttom2, buttom3)
    bot.send_message(message.chat.id, "Hello! ",  reply_markup = markup1)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "cgubenowfimp")

@bot.message_handler(commands=["picture"])
def picture(message):
    img = open("media/41424.png", 'rb')
    bot.send_photo(message.chat.id, img)


@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.lower() == "hi":
        bot.send_message(message.chat.id, "hi")
    elif message.text == "huifa":
        bot.send_message(message.chat.id, "hello")
    elif message.text == "bhfj":
        imp = open("media/picture.jpg", 'rb')
        bot.send_photo(message.chat.id, imp)

    elif message.text in banwords:
        bot.ban_chat_member(message.chat.id, message.from_user.id)
        bot.send_message(message.chat.id, "выгнан")

bot.polling(non_stop=True)