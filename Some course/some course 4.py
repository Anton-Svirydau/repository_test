# set, sorted, filter, lambda, exceptions


""""""


'''
my_set_0 = {1, 2, 3, 4, 5, 6, 7, 8}
print(my_set_0)
print(type(my_set_0))


my_set_1 = set()
for i in range(1, 9):
    my_set_1.add(i)
print(my_set_1)

my_set_1.remove(2)
print(my_set_1)

my_set_1.add(3)
print(my_set_1)
'''

'''
set0 = {1, 2, 3, 4}
set1 = {3, 4, 5, 6}

print(set0.union(set1))
print(set0.intersection(set1))
print(set0.difference(set1))
'''

'''
squares = {x ** 2 for x in range(1, 10)}

print(squares)
'''

'''
# print({1, 2, 3, 3} == {3, 2, 1})

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]

"""
unique_numbers = set(numbers)

print(type(unique_numbers))
print(unique_numbers)
unique_numbers = list(unique_numbers)
print(unique_numbers)
"""

unique_numbers = list(set(numbers))
print(unique_numbers)
print(type(unique_numbers))
'''

'''
fruits = ["banana", "apple", "cherry", "date"]
# sorted_fruits = sorted(fruits)
# sorted_fruits = sorted(fruits, reverse=True)

# print(sorted_fruits)
# print(fruits)


def sort_by_lem(element: str) -> int:
    return len(element)


sorted_fruits = sorted(fruits, key=sort_by_lem)

print(sorted_fruits)
'''

'''
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Diana", "age": 30},
    {"name": "Charlie", "age": 30},
]

"""
def sort_by_age(person: dict) -> int:
    return person["age"]


sorting = sorted(people, key=sort_by_age)
print(sorting)
"""


def sort_by_age_name(element: dict) -> tuple[int, str]:
    return element["age"], element["name"]


sorted_people = sorted(people, key=sort_by_age_name)

print(sorted_people)
'''

'''
def is_even(n: int) -> bool:
    return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filtered_numbers = list(filter(is_even, numbers))

print(type(filtered_numbers))
print(filtered_numbers)
'''

'''
people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 30},
    {"name": "Diana", "age": 19},
    {"name": "Charlie", "age": 40},
]


def is_adult(person: dict) -> bool:
    return person["age"] >= 18


filtered_people = list(filter(is_adult, people))
print(filtered_people)
'''

'''
def sort_by_len(element: str) -> int:
    return len(element)


sort_by_len_lambda = lambda element: len(element)

print(sort_by_len("banana"))
print(sort_by_len_lambda("banana"))
'''

'''
fruits = ["banana", "apple", "cherry", "date"]

"""
sorted_fruits = sorted(fruits, key=lambda element: len(element))

print(sorted_fruits)
"""

longest_word = max(fruits, key=lambda element: len(element))

print(longest_word)
'''

'''
people = [
    {"name": "Alice", "age": 25},
    {"name": "Charlie", "age": 20},
    {"name": "Bob", "age": 20},
    {"name": "Diana", "age": 30},
]

youngest_man = min(people, key=lambda element: (element["age"], element["name"]))

print(youngest_man)
'''


def find_average(*, numbers: list) -> float:
    return sum(numbers) / len(numbers)


try:
    print(find_average(numbers=[1, 2, 3]))
except ZeroDivisionError:
    print("The list is empty")

try:
    print(find_average(numbers=[]))
except ZeroDivisionError as error:
    print(f"Something goes wrong: {error}")

print("We are here")
