from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random

TOKEN = "7519131220:AAEUsqn2XovEMu8b5pEc197V-SBQAK4M2Wo"
list_start = [
    "Words",
    "Tests"
]


bot = TeleBot(TOKEN)

lesson_1 = {
    "и": "and",
    "яблоко": "apple",
    "лампа": "lamp",
    "позволять, допускать": "let",
    "делать, составлять": "make",
    "карта": "map",
    "меня, мне": "me",
    "перо, ручка": "pen",
    "план": "plan",
    "стол, таблица": "table",
    "брать, взять": "take",
    "сказать": "tell",
    "тот, та, то": "that",
    "им, их": "them"
}

lesson_2 = {
    "все, всё": "all",
    "портфель, мешок": "bag",
    "чёрный": "black",
    "книга": "book",
    "ящик, коробка": "box",
    "ребёнок": "child",
    "дети": "children",
    "друг": "friend",
    "давать": "give",
    "хороший": "good",
    "его": "his",
    "в": "in",
    "человек, мужчина": "man",
    "мужчины": "men",
    "мой": "my",
    "заметка, запись": "note",
    "тетрадь, записная книжка": "notebook",
    "на": "on",
    "открывать": "open",
    "карандаш": "pencil",
    "класть, положить": "put",
    "видеть": "see",
    "учить(ся), изучать": "study",
    "хорошо": "well",
    "женщина": "woman",
    "женщины": "women"
}

lesson_3 = {
    "в, на (на вопрос где?)": "at",
    "потому что": "because",
    "низ": "bottom",
    "восток": "east",
    "находить": "find",
    "знать": "know",
    "большой": "large",
    "левый, налево": "left",
    "слева": "on the left",
    "смотреть": "look",
    "означать, значить": "mean",
    "север": "north",
    "наш": "our",
    "полюс": "pole",
    "читать": "read",
    "правый, право": "right",
    "справа": "on the right",
    "море": "sea",
    "сторона": "side",
    "юг": "south",
    "текст": "text",
    "верх": "top",
    "запад": "west",
    "белый": "white",
    "слово": "word",
    "писать": "write",
    "ваш, твой": "your"
}

lesson_4 = {
    "оба": "both",
    "мост": "bridge",
    "здание": "building",
    "называть, звать": "call",
    "город": "city",
    "часы": "clock",
    "соединять": "connect",
    "изогнутый": "curved",
    "конец": "end",
    "перед, передняя сторона, фасад": "front",
    "рука": "hand",
    "больница": "hospital",
    "час": "hour",
    "дом": "house",
    "письмо, буква": "letter",
    "слушать": "listen",
    "жить": "live",
    "близко, близ": "near",
    "почти, около": "nearly",
    "ночь": "night",
    "океан": "ocean",
    "другой": "other",
    "часть": "part",
    "лицо, человек": "person",
    "река": "river",
    "квадратный": "square",
    "бить": "strike",
    "башня": "tower",
    "очень": "very",
    "широкий": "wide",
    "с": "with"
}

lesson_5 = {
    "воздух": "air",
    "почти, едва не": "almost",
    "любой": "any",
    "док": "dock",
    "портовый рабочий": "docker",
    "каждый": "each",
    "летать": "fly",
    "для": "for",
    "от, из": "from",
    "ворота, врата": "gate",
    "уходить, идти, уезжать, направляться": "go",
    "добрый": "kind",
    "род, сорт, класс": "kind",
    "линия": "line",
    "многие": "many",
    "рот, устье (реки)": "mouth",
    "только": "only",
    "или": "or",
    "место": "place",
    "железная дорога": "railway",
    "судно, корабль": "ship",
    "маленький": "small",
    "особый, специальный": "special",
    "там, туда": "there",
    "переводить": "translate",
    "затем": "then",
    "вверх": "up",
    "хотеть, желать": "wish",
    "когда": "when",
    "который": "which",
    "работа, работать": "work",
    "рабочий, работник": "worker",
    "мир": "world"
}

dict_list = [lesson_1, lesson_2, lesson_3, lesson_4, lesson_5]


# def words_test():
#     user_input = ""
#     while user_input != "1":
#         random_dict = random.choice(dict_list)
#         random_key = random.choice(list(random_dict.keys()))
#
#         # Выводим случайный ключ
#         print(f"Переведите слово: {random_key}")
#
#         # Получаем ввод пользователя
#         user_input = input("Ваш ответ: ")
#
#         # Проверяем ответ пользователя
#         if user_input.lower() == random_dict[random_key].lower():
#             print("Правильно")
#         else:
#             print(f"Неправильно, правильный ответ: {random_dict[random_key]}")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(row_width=2)
    for list_start_button in list_start:
        item_button = list_start_button
        markup.add(item_button)
    bot.send_message(message.chat.id, "Choose one", reply_markup=markup)


# @bot.message_handler(func=lambda message: message.text in list_start)
# def send_status_button(message):
#     if message.text == "Words":
#         bot.send_message(message.chat.id, "This option is currently unavailable.")
#     if message.text == "Tests":
#         bot.send_message(message.chat.id, "This option is currently unavailable.")


bot.infinity_polling()
