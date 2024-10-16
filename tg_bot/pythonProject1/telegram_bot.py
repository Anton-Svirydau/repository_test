from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import types

TOKEN = "7519131220:AAEUsqn2XovEMu8b5pEc197V-SBQAK4M2Wo"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_menu(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add("Rules ✊")
    markup.add("Words ✌️")
    markup.add("Tests ✋")
    bot.send_message(message.chat.id, "Hi, dude, choose one", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def initial_choice(message):
    if message.text == "Rules ✊":
        photo = open("botRules.jpg", "rb")
        bot.send_photo(message.chat.id, photo)

    elif message.text == "Words ✌️":
        markup = types.ReplyKeyboardRemove()
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add("10 words 😃", "20 words 🙂", "50 words 😐")
        markup.add("100 words 🥶", "Infinity mode 💀")
        markup.add("Give up 👎")
        bot.send_message(message.chat.id, "Choose mode 😈", reply_markup=markup)

    elif message.text == "Tests ✋":
        bot.send_message(message.chat.id, "Your choose 'Tests ✋'")

    elif message.text == "10 words 😃":
        bot.send_message(message.chat.id, "Your choose '10 words 😃'")

    elif message.text == "20 words 🙂":
        bot.send_message(message.chat.id, "Your choose '20 words 🙂'")

    elif message.text == "50 words 😐":
        bot.send_message(message.chat.id, "Your choose '50 words 😐'")

    elif message.text == "100 words 🥶":
        bot.send_message(message.chat.id, "Your choose '100 words 🥶'")

    elif message.text == "Infinity mode 💀":
        bot.send_message(message.chat.id, "Your choose 'Infinity mode 💀'")

    elif message.text == "Give up 👎":
        markup = types.ReplyKeyboardRemove()
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add("Rules ✊")
        markup.add("Words ✌️")
        markup.add("Tests ✋")
        bot.send_message(message.chat.id, "Buddy, choose one", reply_markup=markup)


bot.infinity_polling()
