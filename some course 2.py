# list, index, for, function, scope
""""""

'''
empty_list = list()
fruits = ["apple", "banana", "cherry"]
my_list = ["apple", 1, 1.5, True, [1, 2, 3]]
print(fruits, len(fruits), my_list)
'''

'''
my_list1 = [1, 2, 3]
my_list2 = [1, 3, 2]
my_list3 = [1, 2, 3]

print(my_list1 == my_list2, my_list1 == my_list3)
'''

'''
# False
print(bool([]))
# True
print(bool([0]))
'''

'''
fruits = ["apple", "banana", "cherry"]
# True False
print("banana" in fruits, "watermelon" in fruits)
'''

'''
element1 = "apple"
element2 = "banana"
element3 = "cherry"
word = "hello"

fruits = [element1, element2, element3]
my_list = list(word)
list1 = fruits + my_list
print(fruits, my_list, list1)
'''

'''
some_list = ["apple", "banana", "cherry"]
print(some_list)  # ['apple', 'banana', 'cherry']
some_list.append("watermelon")
print(some_list)  # ['apple', 'banana', 'cherry', 'watermelon']

my_string = "hello, world"
new_string = my_string.replace("world", "python")

print(my_string, new_string, sep=" / ")
'''

'''
fruits = ["apple", "banana", "cherry"]
fruits2 = ["fig", "grape"]

fruit = fruits.pop()  # fruits.pop()
print(fruit, fruits, sep=" / ")  # print(fruits)

fruits.extend(fruits2)
print(fruits)

fruits.reverse()
print(fruits)
'''

'''
my_list = [5, 4, 8, 10, 1, 2, 14, 4]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
'''

'''
my_string = "My name is Alex"
my_list = my_string.split(" ")

print(my_list)

joined_string = " ".join(my_list)
print(joined_string)
'''

'''
my_list = [3, 6, 2, 4, 1, 187, 21]
print(max(my_list), min(my_list), sum(my_list))
'''

'''
fruits = ["banana", "apple", "cherry", "watermelon"]
print(fruits[0], fruits[-4], fruits[3], fruits[-1], fruits[-3], fruits[-2])

fruits[0] = "pineapple"
fruits[1], fruits[2] = fruits[2], fruits[1]
print(fruits)
'''

'''
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:5])
print(numbers[0:10])  # numbers[0:len(numbers)] / numbers[:]
print(numbers[0:10:2])  # numbers[::2]

new_numbers = numbers[0:5]  # numbers[:5]
print(new_numbers)
print(new_numbers[::-1])
'''

'''
fruits = ["banana", "apple", "cherry", "watermelon"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(fruits[::-1])
fruits.reverse()
print(fruits)

new_numbers = list(reversed(numbers))
print(new_numbers)
'''

'''
file_names = ["document1.txt", "image1.jpg", "document2.txt", "image2.jpg"]
greeting = "Hello, Python"

for file_name in file_names:
    print(file_name)

for char in greeting:
    print(char)
'''

'''
greeting = "Hello, Python"
count_o = 0
for char in greeting:
    if char == "o":
        count_o += 1
        print(char)
print(count_o)
'''

'''
students = ["Alice", "Bob", "Charlie", "David"]

for student in students:
    print(student)
    for char in student:
        print(char)
'''

'''
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

for num in numbers:
    if num == 10:
        break
    print(num)
'''

'''
range_object1 = range(10)
range_object2 = range(1, 10, 2)
range_object3 = range(10, 1, -1)

print(range_object1)
print(range_object2)
print(range_object3)

numbers1 = list(range_object1)
print(numbers1)
numbers2 = list(range_object2)
print(numbers2)
numbers3 = list(range_object3)
print(numbers3)
'''

'''
numbers = [10, 11, 12, 13, 14, 15]

for i in range(len(numbers)):
    numbers[i] += 1

print(numbers)
'''

'''
greeting = "Hello, Python"

indexes = []
count = 0

for i in range(len(greeting)):
    if greeting[i] == "o":
        count += 1
        indexes.append(i)
print(count, indexes)
'''

'''
for i in range(1, 10):
    for j in range(1, 10):
        print(i, " * ", j, " = ", i * j)
'''

'''
numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]


def find_average(numbers):
    average = sum(numbers) / len(numbers)
    return average


average_1 = find_average(numbers_1)
average_2 = find_average(numbers_2)
print(average_1, average_2)
'''

'''
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1

    return count


print(count_vowels("Hello, python"))
print(count_vowels("Python is a very powerful language"))
'''

'''
def nothing():
    print("does nothing")


nothing()
'''

'''
def nothing():
    pass


nothing()
'''

'''
def format_date(*, day: int, month: str) -> str:
    return f"The date is {day} of {month}"


print(format_date(day=15, month="October"))
print(format_date(month="October", day=15))
'''

'''
def custom_greeting(*, name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"


print(custom_greeting(name="John", greeting="Good morning"))
print(custom_greeting(name="John"))
'''

'''
local_var = "not local var"


def my_function():
    # local_var = "I'm local variable"
    print(local_var)


my_function()
print(local_var)
'''

'''
COMFORTABLE_TEMPERATURE = 25


def get_diff_from_comfortable_temperature(*, temperature: int) -> int:
    return COMFORTABLE_TEMPERATURE - temperature


print(get_diff_from_comfortable_temperature(temperature=20))
'''

DEFAULT_LEVEL_EXPERIENCE = 200


def is_leveled_up(*, current_experience: int, gained_experience: int) -> bool:
    total_experience = current_experience + gained_experience
    level_up = False

    if total_experience >= DEFAULT_LEVEL_EXPERIENCE:
        level_up = True

    return level_up


print(is_leveled_up(current_experience=150, gained_experience=60))
print(is_leveled_up(current_experience=10, gained_experience=30))
