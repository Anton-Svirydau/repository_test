from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random
from telebot import types
from eng_dict import test_word
from eng_dict import word_list_test

TOKEN = "7519131220:AAEUsqn2XovEMu8b5pEc197V-SBQAK4M2Wo"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add("Rules")
    markup.add("Words")
    markup.add("Tests")
    bot.send_message(message.chat.id, "Hi, dude, choose one", reply_markup=markup)


global_random_answer = ['-1']
global_random_answer_1 = ['-1']


@bot.message_handler(content_types=["text"])
def initial_choice(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    if message.text == 'Rules':
        photo_0 = open('botRules.jpg', 'rb')
        bot.send_photo(message.chat.id, photo_0)
    elif message.text == 'Words':
        random_word, random_answer = word_list_test()
        global global_random_answer
        global_random_answer = random_answer
        request_answer = f"Translate: {random_word}"
        markup = types.ReplyKeyboardRemove()
        answer_to_user = bot.send_message(message.chat.id, request_answer, reply_markup=markup)
        bot.register_next_step_handler(answer_to_user, words_test_choice)
    elif message.text == 'Tests':
        bot.send_message(message.chat.id, "This option is currently unavailable. 3", reply_markup=markup)

    elif message.text == 'Give up':
        photo_2 = open('botSurrender.jpg', 'rb')
        bot.send_photo(message.chat.id, photo_2)
        markup = types.ReplyKeyboardRemove()
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add("Rules")
        markup.add("Words")
        markup.add("Tests")
        bot.send_message(message.chat.id, "Buddy, choose one", reply_markup=markup)

    elif message.text == 'Once again':
        random_word_1, random_answer_1 = word_list_test()
        global global_random_answer_1
        global_random_answer_1 = random_answer_1
        request_answer_1 = f"Translate: {random_word_1}"
        markup = types.ReplyKeyboardRemove()
        answer_to_user_1 = bot.send_message(message.chat.id, request_answer_1, reply_markup=markup)
        bot.register_next_step_handler(answer_to_user_1, words_test_choice_1)


@bot.message_handler(content_types=["text"])
def words_test_choice(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add('Once again')
    markup.add('Give up')
    if message.text.lower() in global_random_answer:
        photo = open('botTrue.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "You are right", reply_markup=markup)
    else:
        photo_1 = open('botFalse.png', 'rb')
        bot.send_photo(message.chat.id, photo_1)
        bot.send_message(message.chat.id, f"No, bro, are you kidding? 👉 {global_random_answer}", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def words_test_choice_1(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add('Once again')
    markup.add('Give up')
    if message.text.lower() in global_random_answer_1:
        photo = open('botTrue.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "You are right 🎉", reply_markup=markup)
    else:
        photo_1 = open('botFalse.png', 'rb')
        bot.send_photo(message.chat.id, photo_1)
        bot.send_message(message.chat.id, f"No, bro, are you kidding? 👉 {global_random_answer_1}", reply_markup=markup)


bot.infinity_polling()
