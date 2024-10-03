from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7519131220:AAEUsqn2XovEMu8b5pEc197V-SBQAK4M2Wo"
dict_eng = {
    "Words": "Word",
    "Tests": "Tests"
}


bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(row_width=2)
    for eng in dict_eng.keys():
        item_button = KeyboardButton(eng)
        markup.add(item_button)
    bot.send_message(message.chat.id, "Choose one", reply_markup=markup)


bot.infinity_polling()
