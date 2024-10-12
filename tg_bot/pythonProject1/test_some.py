from eng_dict import words_test
from eng_dict import test_word

# words_test()

# abc, bcd = test_word()
#
# print(abc, bcd)

some_list = [
    ["apple", "banana", "grape"],
    ["pen", "pencil", "marker"],
    ["one", "two", "apple"]
]

a = 0

some_word = input()

for some in some_list:
    if some_word in some:
        print("Yes")
        a += 1
        break

if a == 0:
    print("No")
