# set


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
