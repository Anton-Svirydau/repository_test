from telebot import TeleBot

TOKEN = "7519131220:AAEUsqn2XovEMu8b5pEc197V-SBQAK4M2Wo"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, how are doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text)


bot.infinity_polling()
