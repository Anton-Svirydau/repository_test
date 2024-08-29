# print('Hello World')

"""
print('Hello', 'World', end=' ', sep='')
print('Hello', 'World')
print(1)
"""
# input('Please enter something')

'''
name = input('Enter your name: ')
print(name)
'''

'''
name, age = 'Alice', 25
print(name, age)

other_name = name
print(other_name)
'''

'''
x = 3
y = 4

x, y = y, x
print(x, y)
'''

'''
variable_1, variable_2 = 1, "Hype"
print(type(variable_1), type(variable_2))
'''

'''
my_integer1 = 10
my_integer2 = 5
my_float1 = 20.5
my_float2 = 17.5

summary1 = my_integer1 + my_integer2
summary2 = my_float1 + my_float2
multiplication1 = my_integer1 * my_integer2
division1 = my_integer1 / my_integer2
division2 = my_integer1 // my_integer2
division3 = my_integer1 % my_integer2

print(my_integer2 * my_integer2 * my_integer2)
print(my_integer2 ** 3)
print(my_integer1 + my_float1)

print(summary1, summary2, multiplication1, division1, division2, division3)

my_float = float(my_integer1)
print(my_float)

my_float3 = 1.999
my_integer3 = int(my_float3)
my_integer4 = round(my_float3)

print(my_integer3, my_integer4)
'''

'''
apartment = int(input())
entrance = (apartment - 1) // 20 + 1
floor = (apartment - 1) % 20 // 4 + 1

print(entrance, floor)
'''

'''
x = 9
y = 10
z = 10
is_student = True
is_equal = y == z

print(not is_equal)
print(x > y, x != y == z)
'''

'''
print(bool(-1), bool(29), bool('Hello'))
print(bool(0), bool(''))
'''

'''
if True:
    print('Hello')

x = 10
y = 20
if x > 0 and y > 0:
    print('x and y is positive')
elif x < 0:
    print('x is negative')
else:
    print('x is zero')

message = 'Hello'
if message:
    print('message is not empty')
'''

year = 2000

if year % 4 == 0 and year % 100 != 0:
    print('Year is leap')
elif year % 400 == 0:
    print('Year is leap')
else:
    print('Year is not leap')
