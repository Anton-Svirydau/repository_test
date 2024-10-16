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
    "желтый": "yellow"
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
    [["портфель", "мешок", "сумка"], ["bag"]],
    [["чёрный", "чёрная", "черный", "черная"], ["black"]],
    [["книга"], ["book"]],
    [["ящик", "коробка"], ["box"]],
    [["ребёнок", "ребенок"], ["child"]],
    [["дети"], ["children"]],
    ["друг", ["friend"]],
    [["давать"], ["give"]],
    [["хороший", "хорошая"], ["good"]],
    [["его"], ["his"]],
    [["в"], ["in", "into"]],
    [["мужчина"], ["man"]],
    [["мужчины"], ["men"]],
    [["мой", "моя"], ["my"]],
    [["заметка", "запись"], ["note"]],
    [["тетрадь", "записная книжка"], ["notebook"]],
    [["на"], ["on", "onto"]],
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
    [["потому что"], ["because"]],
    [["низ"], ["bottom"]],
    [["восток"], ["east"]],
    [["находить"], ["find"]],
    [["знать"], ["know"]],
    [["большой", "большая"], ["large", "big"]],
    [["левый", "налево", "левая"], ["left"]],
    [["смотреть"], ["look"]],
    [["означать", "значить"], ["mean"]],
    [["север"], ["north"]],
    [["наш", "наша"], ["our"]],
    [["полюс"], ["pole"]],
    [["читать"], ["read"]],
    [["правый, право", "правая"], ["right"]],
    [["море"], ["sea"]],
    [["сторона"], ["side"]],
    [["юг"], ["south"]],
    [["текст"], ["text"]],
    [["верх"], ["top"]],
    [["запад"], ["west"]],
    [["белый", "белая"], ["white"]],
    [["слово"], ["word"]],
    [["писать"], ["write"]],
    [["ваш", "твой", "ваша", "твоя"], ["your"]]
]

lesson_4_list = [
    [["оба", "обе"], ["both"]],
    [["мост"], ["bridge"]],
    [["здание"], ["building"]],
    [["называть", "звать"], ["call"]],
    [["город"], ["city"]],
    [["часы"], ["clock", "watch"]],
    [["соединять"], ["connect"]],
    [["изогнутый", "изогнутая"], ["curved"]],
    [["конец"], ["end"]],
    [["перед", "передняя сторона", "фасад"], ["front"]],
    [["рука"], ["hand"]],
    [["больница"], ["hospital"]],
    [["час"], ["hour"]],
    [["дом"], ["house"]],
    [["письмо", "буква"], ["letter"]],
    [["слушать"], ["listen"]],
    [["жить"], ["live"]],
    [["близко", "близ"], ["near"]],
    [["ночь"], ["night"]],
    [["океан"], ["ocean"]],
    [["другой", "другая"], ["other"]],
    [["часть"], ["part"]],
    [["лицо", "человек"], ["person"]],
    [["река"], ["river"]],
    [["квадратный", "квадратная"], ["square"]],
    [["бить"], ["strike"]],
    [["башня"], ["tower"]],
    [["очень"], ["very"]],
    [["широкий", "широкая"], ["wide"]],
    [["с"], ["with"]]
]

lesson_5_list = [
    [["воздух"], ["air"]],
    [["почти"], ["almost", "nearly"]],
    [["любой", "любая"], ["any"]],
    [["каждый", "каждая"], ["every", "each"]],
    [["летать"], ["fly"]],
    [["для"], ["for"]],
    [["от", "из"], ["from"]],
    [["ворота", "врата"], ["gate"]],
    [["уходить", "идти", "уезжать", "направляться"], ["go"]],
    [["добрый", "добрая", "род", "сорт", "класс"], ["kind"]],
    [["линия"], ["line"]],
    [["многие"], ["many"]],
    [["рот", "устье"], ["mouth"]],
    [["только"], ["only"]],
    [["или"], ["or"]],
    [["место"], ["place"]],
    [["железная дорога"], ["railway"]],
    [["судно", "корабль"], ["ship"]],
    [["маленький", "маленькая"], ["small", "little"]],
    [["особый", "специальный", "особая", "специальная"], ["special"]],
    [["там", "туда"], ["there"]],
    [["переводить"], ["translate"]],
    [["затем"], ["then"]],
    [["вверх"], ["up"]],
    [["хотеть", "желать"], ["wish", "want"]],
    [["когда"], ["when"]],
    [["который", "которая"], ["which"]],
    [["работа", "работать"], ["work"]],
    [["рабочий", "работник"], ["worker"]],
    [["мир"], ["world"]]
]

lesson_6_list = [
    [["вдоль"], ["along"]],
    [["также"], ["also", "too"]],
    [["как"], ["as"]],
    [["красивый", "красивая"], ["beautiful"]],
    [["самый лучший", "самая лучшая"], ["best"]],
    [["столица"], ["capital"]],
    [["церковь"], ["church"]],
    [["кинотеатр", "кино"], ["cinema"]],
    [["страна"], ["country"]],
    [["знаменитый", "знаменитая"], ["famous"]],
    [["иностранный", "иностранная"], ["foreign"]],
    [["прежний", "бывший", "прежняя", "бывшая"], ["former"]],
    [["слышать"], ["hear"]],
    [["холм", "возвышенность"], ["hill"]],
    [["дом", "родина"], ["home"]],
    [["список", "перечень"], ["list"]],
    [["главный", "основной", "главная", "основная"], ["main"]],
    [["большая часть", "большинство"], ["most"]],
    [["новый", "новая"], ["new"]],
    [["теперь", "сейчас"], ["now"]],
    [["часто"], ["often"]],
    [["старый", "старая"], ["old"]],
    [["дворец"], ["palace"]],
    [["народ", "люди"], ["people"]],
    [["тюрьма"], ["prison"]],
    [["королева"], ["queen"]],
    [["королевский", "королевская"], ["royal"]],
    [["магазин"], ["shop"]],
    [["улица"], ["street"]],
    [["вещь", "предмет"], ["thing"]],
    [["сквозь", "через"], ["through"]],
    [["сегодня", "в наше время"], ["today"]],
    [["посещать", "посещение"], ["visit"]],
    [["ходить пешком", "гулять"], ["walk"]]
]

lesson_7_list = [
    [["животное"], ["animal"]],
    [["осень"], ["autumn"]],
    [["обратно"], ["back"]],
    [["начинать", "начинаться"], ["begin"]],
    [["птица"], ["bird"]],
    [["коричневый", "коричневая"], ["brown"]],
    [["но"], ["but"]],
    [["холодный", "холодная"], ["cold"]],
    [["прохладный", "прохладная"], ["cool"]],
    [["урожай"], ["crop"]],
    [["различный", "различная"], ["different"]],
    [["падать"], ["fall"]],
    [["цветок"], ["flower"]],
    [["зеленый", "зеленая"], ["green"]],
    [["расти", "растить", "выращивать"], ["grown"]],
    [["держать", "держаться"], ["keep"]],
    [["лист"], ["leaf"]],
    [["листья"], ["leaves"]],
    [["месяц"], ["month"]],
    [["дождь"], ["rain"]],
    [["красный", "красная"], ["red"]],
    [["время года", "сезон"], ["season"]],
    [["снег"], ["snow"]],
    [["некоторый", "некоторая"], ["some"]],
    [["иногда"], ["sometimes"]],
    [["весна"], ["spring"]],
    [["буря"], ["strom"]],
    [["лето"], ["summer"]],
    [["дерево"], ["tree"]],
    [["обычно"], ["usually"]],
    [["овощ", "растительный", "растительная"], ["vegetable"]],
    [["теплый", "теплая"], ["warm"]],
    [["вода"], ["water"]],
    [["погода"], ["weather"]],
    [["ветер"], ["wind"]],
    [["зима"], ["winter"]],
    [["желтый", "желтая"], ["yellow"]]
]

lesson_8_list = [
    [["отвечать", "ответ"], ["answer"]],
    [["спросить"], ["ask"]],
    [["мальчик", "парень"], ["boy"]],
    [["купить"], ["buy"]],
    [["центральный", "центральная"], ["central"]],
    [["культура"], ["culture"]],
    [["танцевать", "танец"], ["dance"]],
    [["день"], ["day"]],
    [["платье"], ["dress"]],
    [["есть"], ["eat"]],
    [["прекрасный", "прекрасная"], ["fine"]],
    [["девочка", "девушка"], ["girl"]],
    [["земля", "грунт"], ["ground"]],
    [["здесь", "тут"], ["here"]],
    [["любить", "нравиться"], ["like"]],
    [["нет"], ["no"]],
    [["тихий", "тишина", "покой", "тихая"], ["quiet"]],
    [["отдых"], ["recreation", "rest"]],
    [["комната", "пространство"], ["room"]],
    [["сказать"], ["say"]],
    [["сидеть"], ["sit"]],
    [["станция"], ["station"]],
    [["думать"], ["think"]],
    [["время", "раз"], ["time"]],
    [["подземный", "метро", "подземная"], ["underground"]],
    [["путь", "способ"], ["way"]],
    [["да"], ["yes"]]
]

lesson_9_list = [

]

list_with_lesson_lists = (lesson_1_list + lesson_2_list + lesson_3_list + lesson_4_list + lesson_5_list +
                          lesson_6_list + lesson_7_list + lesson_8_list)


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
    random_list = random.choice(list_with_lesson_lists)
    random_ru_or_eng = random.choice(random_list)
    random_word = random.choice(random_ru_or_eng)

    print(f"Translate: {random_word}")

    user_input = input("Your answer: ")

    if random_ru_or_eng == random_list[0]:
        if user_input.lower() in random_list[1]:
            print("True")
        else:
            print(f"False -> {random_list[1]}")
    if random_ru_or_eng == random_list[1]:
        if user_input.lower() in random_list[0]:
            print("True")
        else:
            print(f"False -> {random_list[0]}")


def word_list_test():
    random_list = random.choice(list_with_lesson_lists)
    random_ru_or_eng = random.choice(random_list)
    random_word = random.choice(random_ru_or_eng)

    if random_ru_or_eng == random_list[0]:
        return random_word, random_list[1]
    if random_ru_or_eng == random_list[1]:
        return random_word, random_list[0]


def x_random(x):
    cnt = 0

    for i in range(x):
        random_list = random.choice(list_with_lesson_lists)
        random_ru_or_eng = random.choice(random_list)
        random_word = random.choice(random_ru_or_eng)

        print(f"Translate: {random_word}")

        user_input = input("Your answer: ")

        if random_ru_or_eng == random_list[0]:
            if user_input.lower() in random_list[1]:
                print("True")
                cnt += 1
            else:
                print(f"False -> {random_list[1]}")
        if random_ru_or_eng == random_list[1]:
            if user_input.lower() in random_list[0]:
                print("True")
                cnt += 1
            else:
                print(f"False -> {random_list[0]}")

    print(f"Right answer: {cnt}")


def random_words_choose(x):
    random_words_list = []
    translation_option = []

    for i in range(x):
        random_list = random.choice(list_with_lesson_lists)
        random_ru_or_eng = random.choice(random_list)
        random_word = random.choice(random_ru_or_eng)

        random_words_list += [random_word]

        if random_ru_or_eng == random_list[0]:
            translation_option += [random_list[1]]
        if random_ru_or_eng == random_list[1]:
            translation_option += [random_list[0]]

    return random_words_list, translation_option
