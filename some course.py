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

'''
year = 2000

if year % 4 == 0 and year % 100 != 0:
    print('Year is leap')
elif year % 400 == 0:
    print('Year is leap')
else:
    print('Year is not leap')
'''

'''
my_string = """Hello
world
123"""
print(my_string)

first_name = 'Anton'
second_name = 'Smith'
print(first_name + ' ' + second_name)
print(len(first_name))

my_integer = 100
my_string = str(my_integer)
print(my_string)
my_integer1 = int(my_string)
print(my_integer1)

my_string1 = input('Enter a number: ')
print(type(my_string1))
'''

'''
big_integer = 2 ** 1000
print(len(str(big_integer)))

my_string = 'Hello'

print('Hello' in my_string)
print('hello' in my_string)
'''

'''
my_string1 = 'Alice'
my_string2 = '   Hello, world!    '
my_string3, my_string4 = '10', '10x'

print(my_string1.upper())
print(my_string1.lower())
print(my_string2)
print(my_string2.strip())
print(my_string2.replace('world', 'Python'))
print(my_string2.count('l'), my_string2.count('rl'), my_string2.count('R'))
print(my_string3.isdigit(), my_string4.isdigit())
'''

'''
integer = input('Enter a number: ')
if integer.isdigit():
    integer = int(integer)

print(type(integer))
'''

'''
name = 'Alice'
age = 25
print(f"Hello, my name is {name}. I'm {age} years old")

x = 10
y = 5
print(f"summary is {x + y}, multiplication is {x * y}")
'''

'''
my_string = input("Enter a number: ")

if my_string.isdigit():
    my_integer = int(my_string)
    print(my_integer)
else:
    print(f"{my_string} is not a number")
'''

'''
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

txt1 = "My name is {name}, I'm {age}".format(name="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)
print(txt1)
print(txt2)
print(txt3)
'''

# :> Left aligns the result (within the available space)
txt = "We have {:>8} chickens."
print(txt.format(49))
# :< Right aligns the result (within the available space)
txt = "We have {:<8} chickens."
print(txt.format(49))
# :^ Center aligns the result (within the available space)
txt = "We have {:^8} chickens."
print(txt.format(49))
# := Places the sign to the left most position
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))
# :+ Use a plus sign to indicate if the result is positive or negative
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))
# :- Use a minus sign for negative values only
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))
# :  Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))
# :, Use a comma as a thousand separator
txt = "The universe is {:,} years old."
print(txt.format(13800000000))
# :_ Use underscore as a thousand separator
txt = "The universe is {:_} years old."
print(txt.format(13800000000))
# :b Binary format
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))
# :c Converts the value into the corresponding unicode character
# :d Decimal format
txt = "We have {:d} chickens."
print(txt.format(0b101))
# :e Scientific format, with a lower case e
txt = "We have {:e} chickens."
print(txt.format(5))
# :E Scientific format, with an upper case E
txt = "We have {:E} chickens."
print(txt.format(5))
# :f Fix point number format
txt = "The price is {:.2f} dollars."
print(txt.format(45))
txt = "The price is {:f} dollars."
print(txt.format(45))
# :F Fix point number format, in uppercase format (show inf and nan as INF and NAN)
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))
txt = "The price is {:f} dollars."
print(txt.format(x))
# :g General format
# :G General format (using upper case E for scientific notations)
# :o Octal format
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))
# :x Hex format, lower case
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))
# :X Hex format, upper case
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))
# :n Number format
# :% Percentage format
txt = "You scored {:%}"
print(txt.format(0.25))
txt = "You scored {:.0%}"
print(txt.format(0.25))
