from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import types
from eng_dict import random_words_choose
from eng_dict import word_list_test

TOKEN = "7519131220:AAEUsqn2XovEMu8b5pEc197V-SBQAK4M2Wo"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_menu(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add("Rules ✊")
    markup.add("Words ✌️")
    markup.add("Tests ✋")
    bot.send_message(message.chat.id, "Hi, dude, choose one", reply_markup=markup)


user_values = []
translation_option = []
translation_option_10 = []
random_words_list = []
random_words_list_10 = []
translation_option_20 = []
random_words_list_20 = []
translation_option_50 = []
random_words_list_50 = []
translation_option_100 = []
random_words_list_100 = []
right_answer = 0
amount_words_test = 0


@bot.message_handler(content_types=["text"])
def initial_choice(message):
    global user_values
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
        bot.send_message(message.chat.id, "Your choose 'Tests ✋'")

    elif message.text == "10 words 😃":
        global random_words_list_10
        global translation_option_10
        amount_words_test = 10
        markup = types.ReplyKeyboardRemove()
        random_words_list_10, translation_option_10 = random_words_choose(10)
        random_words_list = random_words_list_10
        translation_option = translation_option_10
        answer_to_user = bot.send_message(message.chat.id, f"Translate: {random_words_list_10[len(user_values)]}",
                                          reply_markup=markup)
        bot.register_next_step_handler(answer_to_user, random_check)

    elif message.text == "20 words 🙂":
        global random_words_list_20
        global translation_option_20
        amount_words_test = 20
        markup = types.ReplyKeyboardRemove()
        random_words_list_20, translation_option_20 = random_words_choose(20)
        random_words_list = random_words_list_20
        translation_option = translation_option_20
        answer_to_user = bot.send_message(message.chat.id, f"Translate: {random_words_list_20[len(user_values)]}",
                                          reply_markup=markup)
        bot.register_next_step_handler(answer_to_user, random_check)

    elif message.text == "50 words 😐":
        global random_words_list_50
        global translation_option_50
        amount_words_test = 50
        markup = types.ReplyKeyboardRemove()
        random_words_list_50, translation_option_50 = random_words_choose(50)
        random_words_list = random_words_list_50
        translation_option = translation_option_50
        answer_to_user = bot.send_message(message.chat.id, f"Translate: {random_words_list_50[len(user_values)]}",
                                          reply_markup=markup)
        bot.register_next_step_handler(answer_to_user, random_check)

    elif message.text == "100 words 🥶":
        global random_words_list_100
        global translation_option_100
        amount_words_test = 100
        markup = types.ReplyKeyboardRemove()
        random_words_list_100, translation_option_100 = random_words_choose(100)
        random_words_list = random_words_list_100
        translation_option = translation_option_100
        answer_to_user = bot.send_message(message.chat.id, f"Translate: {random_words_list_100[len(user_values)]}",
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
    global user_values
    global right_answer
    if message.text.lower() in translation_option[len(user_values)]:
        right_answer += 1
        bot.send_message(message.chat.id, "✅ You are right ✅", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"❌ No, bro, are you kidding? ❌ 👉 "
                                          f"{', '.join(map(str, translation_option[len(user_values)]))}",
                         reply_markup=markup)

    if len(user_values) < amount_words_test - 1:
        user_values += ["1"]
        answer_to_user = bot.send_message(message.chat.id, f"Translate: {random_words_list[len(user_values)]}",
                                          reply_markup=markup)
        bot.register_next_step_handler(answer_to_user, random_check)
    else:
        user_values = []
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


bot.infinity_polling()
