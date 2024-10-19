from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import types
from eng_dict import random_words_choose
from eng_dict import word_list_test
from googletrans import Translator
import random

TOKEN = "7519131220:AAEUsqn2XovEMu8b5pEc197V-SBQAK4M2Wo"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_menu(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add("Rules ✊")
    markup.add("Words ✌️")
    markup.add("Tests ✋")
    bot.send_message(message.chat.id, "Hi, dude, choose one", reply_markup=markup)


user_values_cnt = []
translation_option = []
random_words_list = []
right_answer = 0
amount_words_test = 0
translator = Translator()
eng_list = ["table", "let", "take"]
current_word = "-1"


@bot.message_handler(content_types=["text"])
def initial_choice(message):
    global user_values_cnt
    global random_words_list
    global translation_option

    if message.text == "Rules ✊":
        photo = open("botRules.jpg", "rb")
        bot.send_photo(message.chat.id, photo)

    elif message.text == "Words ✌️":
        global right_answer
        right_answer = 0
        global amount_words_test
        amount_words_test = 0
        markup = types.ReplyKeyboardRemove()
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add("10 words 😃", "20 words 🙂", "50 words 😐")
        markup.add("100 words 🥶", "Infinity mode 💀")
        markup.add("Give up 👎")
        bot.send_message(message.chat.id, "Choose mode 😈", reply_markup=markup)

    elif message.text == "Tests ✋":
        global current_word
        markup = types.ReplyKeyboardRemove()
        current_word = random.choice(eng_list)
        ask_word = bot.send_message(message.chat.id, f"Translate: {current_word}", reply_markup=markup)
        bot.register_next_step_handler(ask_word, check_translation)

    elif message.text == "10 words 😃":
        amount_words_test = 10
        markup = types.ReplyKeyboardRemove()
        random_words_list, translation_option = random_words_choose(10)
        answer_to_user = bot.send_message(message.chat.id, f"Translate: {random_words_list[len(user_values_cnt)]}",
                                          reply_markup=markup)
        bot.register_next_step_handler(answer_to_user, random_check)

    elif message.text == "20 words 🙂":
        amount_words_test = 20
        markup = types.ReplyKeyboardRemove()
        random_words_list, translation_option = random_words_choose(20)
        answer_to_user = bot.send_message(message.chat.id, f"Translate: {random_words_list[len(user_values_cnt)]}",
                                          reply_markup=markup)
        bot.register_next_step_handler(answer_to_user, random_check)

    elif message.text == "50 words 😐":
        amount_words_test = 50
        markup = types.ReplyKeyboardRemove()
        random_words_list, translation_option = random_words_choose(50)
        answer_to_user = bot.send_message(message.chat.id, f"Translate: {random_words_list[len(user_values_cnt)]}",
                                          reply_markup=markup)
        bot.register_next_step_handler(answer_to_user, random_check)

    elif message.text == "100 words 🥶":
        amount_words_test = 100
        markup = types.ReplyKeyboardRemove()
        random_words_list, translation_option = random_words_choose(100)
        answer_to_user = bot.send_message(message.chat.id, f"Translate: {random_words_list[len(user_values_cnt)]}",
                                          reply_markup=markup)
        bot.register_next_step_handler(answer_to_user, random_check)

    elif message.text == "Infinity mode 💀":
        markup = types.ReplyKeyboardRemove()
        random_words_list, translation_option = word_list_test()
        answer_to_user = bot.send_message(message.chat.id, f"Translate: {random_words_list}", reply_markup=markup)
        bot.register_next_step_handler(answer_to_user, infinity_check)

    elif message.text == "Give up 👎":
        markup = types.ReplyKeyboardRemove()
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add("Rules ✊")
        markup.add("Words ✌️")
        markup.add("Tests ✋")
        bot.send_message(message.chat.id, "Buddy, choose one", reply_markup=markup)

    elif message.text == "Once again 🗿":
        markup = types.ReplyKeyboardRemove()
        random_words_list, translation_option = word_list_test()
        answer_to_user = bot.send_message(message.chat.id, f"Translate: {random_words_list}", reply_markup=markup)
        bot.register_next_step_handler(answer_to_user, infinity_check)


@bot.message_handler(content_types=["text"])
def random_check(message):
    markup = types.ReplyKeyboardRemove()
    global user_values_cnt
    global right_answer
    if message.text.lower() in translation_option[len(user_values_cnt)]:
        right_answer += 1
        bot.send_message(message.chat.id, "✅ You are right ✅", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"❌ No, bro, are you kidding? ❌ 👉 "
                                          f"{', '.join(map(str, translation_option[len(user_values_cnt)]))}",
                         reply_markup=markup)

    if len(user_values_cnt) < amount_words_test - 1:
        user_values_cnt += ["1"]
        answer_to_user = bot.send_message(message.chat.id, f"Translate: {random_words_list[len(user_values_cnt)]}",
                                          reply_markup=markup)
        bot.register_next_step_handler(answer_to_user, random_check)
    else:
        user_values_cnt = []
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add("Rules ✊")
        markup.add("Words ✌️")
        markup.add("Tests ✋")
        if right_answer / amount_words_test >= 0.9:
            bot.send_message(message.chat.id, f"Buddy, your right answer: {right_answer}/{amount_words_test}👍",
                             reply_markup=markup)
        else:
            bot.send_message(message.chat.id, f"Buddy, your right answer: {right_answer}/{amount_words_test} 👎",
                             reply_markup=markup)


@bot.message_handler(content_types=["text"])
def infinity_check(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add('Once again 🗿')
    markup.add('Give up 👎')
    if message.text.lower() in translation_option:
        bot.send_message(message.chat.id, "✅ You are right ✅", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"❌ No, bro, are you kidding? ❌ 👉 {translation_option}", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def check_translation(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add("Rules ✊")
    markup.add("Words ✌️")
    markup.add("Tests ✋")
    translation = translator.translate(current_word, src='en', dest='ru').text.lower()
    if message.text.lower() == translation:
        bot.send_message(message.chat.id, "True", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"No, true is: {translation}", reply_markup=markup)


bot.infinity_polling()
