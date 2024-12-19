# from eng_dict import words_test
# from eng_dict import test_word
# from eng_dict import world_test_list
# from eng_dict import word_list_test
# from eng_dict import x_random
# from eng_dict import random_words_choose
from googletrans import Translator
from timeit import default_timer as timer

# words_test()
#
# abc, bcd = test_word()
#
# print(abc, bcd)

# some_list = [
#     ["apple", "banana", "grape"],
#     ["pen", "pencil", "marker"],
#     ["one", "two", "apple"]
# ]
#
# a = 0
#
# some_word = input()
#
# for some in some_list:
#     if some_word in some:
#         print("Yes")
#         a += 1
#         break
#
# if a == 0:
#     print("No")
#
# world_test_list()
#
# some_word, some_list = word_list_test()
# print(some_word, some_list)
#
# x_random(10)
#
# a, b = random_words_choose(3)
# print(a)
# print(b)


translator = Translator()

src = 'en'
dest = 'ru'

text = "space"
translate_1 = input()

start = timer()

translated_text = translator.translate(translate_1, src=src, dest=dest).text

print(translated_text)

end = timer()
print(f"Время выполнения: {end - start:.5f} секунд")


def prnt():
    some = 1
    if some == 1:
        print("some = 1")
    else:
        print("something wrong ;(")
    return some
