# list

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

my_list = [3, 6, 2, 4, 1, 187, 21]
print(max(my_list), min(my_list), sum(my_list))
