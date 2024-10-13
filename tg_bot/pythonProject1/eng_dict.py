import random


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
    "каждый": "every",
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

lesson_6 = {
    "вдоль, по": "along",
    "также": "also",
    "как; когда, в то время как": "as",
    "красивый, прекрасный": "beautiful",
    "самый лучший": "best",
    "столица": "capital",
    "церковь": "church",
    "кинотеатр, кино": "cinema",
    "страна": "country",
    "делать": "do",
    "знаменитый": "famous",
    "иностранный": "foreign",
    "прежний, бывший": "former",
    "слышать": "hear",
    "холм, возвышенность; гора": "hill",
    "дом; родина": "home",
    "список, перечень": "list",
    "главный, основной": "main",
    "большая часть": "most",
    "новый": "new",
    "теперь, сейчас": "now",
    "часто": "often",
    "старый": "old",
    "дворец": "palace",
    "народ, люди": "people",
    "тюрьма": "prison",
    "королева": "queen",
    "королевский": "royal",
    "магазин": "shop",
    "улица": "street",
    "вещь, предмет": "thing",
    "сквозь, через": "through",
    "сегодня, в наше время": "today",
    "посещать; посещение": "visit",
    "ходить пешком, гулять": "walk"
}

lesson_7 = {
    "животное": "animal",
    "осень": "autumn",
    "обратно": "back",
    "начинать(ся)": "begin",
    "птица": "bird",
    "коричневый": "brown",
    "но": "but",
    "холодный": "cold",
    "прохладный": "cool",
    "урожай": "crop",
    "различный": "different",
    "падать": "fall",
    "цветок": "flower",
    "зеленый": "green",
    "расти, растить; выращивать, становиться": "grown",
    "держать(ся); хранить, оставаться, сохранять; вести": "keep",
    "лист": "leaf",
    "листья": "leaves",
    "месяц": "month",
    "дождь": "rain",
    "красный": "red",
    "время года, сезон": "season",
    "снег": "snow",
    "некоторый": "some",
    "иногда": "sometimes",
    "весна": "spring",
    "буря": "strom",
    "лето": "summer",
    "слишком, также": "too",
    "дерево": "tree",
    "обычно": "usually",
    "овощ, растительный": "vegetable",
    "теплый": "warm",
    "вода": "water",
    "погода": "weather",
    "ветер": "wind",
    "зима": "winter",
    "желтый": "yellow",
}

lesson_8 = {
    "отвечать, ответ": "answer",
    "спросить": "ask",
    "мальчик, парень": "boy",
    "купить": "buy",
    "центральный": "central",
    "культура": "culture",
    "танцевать, танец": "dance",
    "день": "day",
    "платье; одежда; одевать(ся)": "dress",
    "есть, съедать": "eat",
    "прекрасный; изящный": "fine",
    "девочка, девушка": "girl",
    "земля, грунт": "ground",
    "здесь, тут": "here",
    "любить, нравиться": "like",
    "нет": "no",
    "тихий, спокойный; тишина, покой": "quiet",
    "развлечение, отдых": "recreation",
    "отдых; отдыхать": "rest",
    "комната, пространство": "room",
    "сказать": "say",
    "сидеть": "sit",
    "станция, стоянка, пост; база": "station",
    "думать": "think",
    "время; раз": "time",
    "подземный, метро": "underground",
    "путь, средство, способ": "way",
    "да": "yes"
}

dict_list = [lesson_1, lesson_2, lesson_3, lesson_4, lesson_5, lesson_6, lesson_7, lesson_8]
# user_input = ""

lesson_1_list = [
    [["и"], ["and"]],
    [["яблоко"], ["apple"]],
    [["лампа"], ["lamp"]],
    [["позволять", "допускать"], ["let"]],
    [["делать"], ["do", "make"]],
    [["карта"], ["map"]],
    [["меня", "мне"], ["me"]],
    [["перо", "ручка"], ["pen"]],
    [["план"], ["plan"]],
    [["стол", "таблица"], ["table"]],
    [["брать", "взять"], ["take"]],
    [["сказать"], ["tell"]],
    [["тот", "та", "то"], ["that"]],
    [["им", "их"], ["them"]]
]

lesson_2_list = [
    [["все", "всё"], ["all"]],
    [["портфель", "мешок"], ["bag"]],
    [["чёрный"], ["black"]],
    [["книга"], ["book"]],
    [["ящик", "коробка"], ["box"]],
    [["ребёнок"], ["child"]],
    [["дети"], ["children"]],
    ["друг", ["friend"]],
    [["давать"], ["give"]],
    [["хороший"], ["good"]],
    [["его"], ["his"]],
    [["в"], ["in"]],
    [["человек", "мужчина"], ["man"]],
    [["мужчины"], ["men"]],
    [["мой"], ["my"]],
    [["заметка", "запись"], ["note"]],
    [["тетрадь", "записная книжка"], ["notebook"]],
    [["на"], ["on"]],
    [["открывать"], ["open"]],
    [["карандаш"], ["pencil"]],
    [["класть", "положить"], ["put"]],
    [["видеть"], ["see"]],
    [["учить", "учиться", "изучать"], ["study"]],
    [["хорошо"], ["well"]],
    [["женщина"], ["woman"]],
    [["женщины"], ["women"]]
]

lesson_3_list = [

]

list_lists = lesson_1_list + lesson_2_list


def words_test():
    user_input = ""
    while user_input != "stop":
        random_dict = random.choice(dict_list)
        random_key = random.choice(list(random_dict.keys()))

        # Выводим случайный ключ
        print(f"Переведите слово: {random_key}")

        # Получаем ввод пользователя
        user_input = input("Ваш ответ: ")

        # Проверяем ответ пользователя
        if user_input.lower() == random_dict[random_key].lower():
            print("Правильно")
        else:
            print(f"Неправильно, правильный ответ: {random_dict[random_key]}")


# words_test()

def test_word():
    random_dict = random.choice(dict_list)
    random_key = random.choice(list(random_dict.keys()))
    return random_key, random_dict[random_key]


def world_test_list():
    random_list = random.choice(list_lists)
    random_ru_or_eng = random.choice(random_list)
    random_word = random.choice(random_ru_or_eng)

    print(f"Translate: {random_word}")

    user_input = input("Your answer: ")

    if random_ru_or_eng == random_list[0]:
        if user_input.lower() in random_list[1]:
            print("True")
        else:
            print("False")
    if random_ru_or_eng == random_list[1]:
        if user_input.lower() in random_list[0]:
            print("True")
        else:
            print("False")
