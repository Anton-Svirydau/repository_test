# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
from random import randint
"""
interest_rate = 1.01
initial_debt = 1000

def calculate_debt(days):
  if days < 0:
    print('cringe :(')
    return 0

  if days == 0:
    return initial_debt

  debt_yesterday = calculate_debt(days - 1)
  return debt_yesterday * interest_rate

print('+/-', int(calculate_debt(300)), '$')


def reverse_sequence():
  num = int(input())
  if num != -1:
    reverse_sequence()
    print(num)


reverse_sequence()
"""

'''
class Person:
  def __init__(self):
    print("Create object Person")

tom = Person()
'''

'''
class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age


tom = Person("Tom", 22)
bob = Person("Bob", 43)

print(tom.name)  
print(bob.name) 
'''

'''
class Person:

  def __init__(self, name):
    self.name = name
    print("Create", self.name)

  def __del__(self):
    print("Delete", self.name)


tom = Person("Tom")
'''

'''
class MyClass:
  @staticmethod
  def static_method():
    print("This is a static method in a class")


MyClass.static_method()
'''

'''
class Calculator:
  @staticmethod
  def add_numbers(x, y):
    return x + y


result = Calculator.add_numbers(3, 5)
print(result)
'''

'''
class Math:
  @staticmethod
  def add(x, y):
    return x + y

  @staticmethod
  def subtract(x, y):
    return x - y

print(Math.add(2, 3))
print(Math.subtract(5, 2))
'''

'''
class StringUtils:
  @staticmethod
  def reverse_string(string):
    return string[::-1]

result = StringUtils.reverse_string('string')
print(result)
'''
'''
class MathUtils:
    _fib_cache = {0: 0, 1: 1}

    @staticmethod
    def fibonacci(n):
        if n not in MathUtils._fib_cache:
            MathUtils._fib_cache[n] = MathUtils.fibonacci(n - 1) + MathUtils.fibonacci(n - 2)
        return MathUtils._fib_cache[n]

result = MathUtils.fibonacci(3)
print(result)
'''
'''
class StringUtils:
    @staticmethod
    def reverse_string(string):
        return string[::-1]

class TextUtils:
    @staticmethod
    def reverse_and_uppercase(string):
        reversed_string = StringUtils.reverse_string(string)
        return reversed_string.upper()

result = TextUtils.reverse_and_uppercase("Hello World")
print(result)
'''
'''
class Functions:
    @staticmethod
    def calculate_debt(days):
        if days == 0:
            return 1000

        return Functions.calculate_debt(days - 1) * 1.01

    @staticmethod
    def reverse_sequence():
        num = int(input())
        if num != -1:
            Functions.reverse_sequence()
            print(num)

print(int(Functions.calculate_debt(300)))

Functions.reverse_sequence()
'''
'''
class Factorial:
    @staticmethod
    def recursive(n):
        if n == 1:
            return n
        else:
            return n * Factorial.recursive(n - 1)

    @staticmethod
    def iterative(n):
        i = 1
        result = 1

        for i in range(1, n + 1):
            result *= i

        return result

print(Factorial.recursive(10))
print(Factorial.iterative(10))

print(Factorial().recursive(10))
print(Factorial().iterative(10))
'''
'''
def gcd_recursive(a, b):
    min_num = min(a, b)
    max_num = max(a, b)

    if min_num == 0:
        return max_num
    elif min_num == 1:
        return 1
    else:
        return gcd_recursive(min_num, max_num % min_num)
a, b = int(input()), int(input())
print(gcd_recursive(a, b))
'''
'''
def gcd_iter(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return b
a, b = int(input()), int(input())
print(gcd_iter(a, b))
'''
'''
import math
a, b = int(input()), int(input())
print(math.gcd(a, b))
'''
'''
import random

array_size = 20
random_array = [random.randint(0, 99) for _ in range(array_size)]
print(*random_array)

def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True

    return arr

print(*bubble_sort(random_array))

def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr

print(*selection_sort(random_array))
'''

'''
def sort_array(arr):
    return sorted(arr)


numbers = [5, 25, 9, 16, 1, 4]
print(*sort_array(numbers))

strings = ["kek", "omg", "lol", "cringe"]
print(*sort_array(strings))
'''

'''
a = list(map(int, input().split()))
k = int(input())

for _ in range(k):
    t, x = map(int, input().split())
    if t == 1:
        for i in range(len(a)):
            if a[i] % x == 0:
                a[i] += 1
    else:
        s = 0
        for i in range(len(a)):
            if a[i] % x == 0:
                s += a[i]
        print(s)
'''

'''
student_amount = int(input())

names = []
grades = []
for student_idx in range(student_amount):
    name, grade = input().split()
    names.append(name)
    grades.append(int(grade))

for student_i in range(student_amount):
    for student_j in range(student_amount):
        if grades[student_i] > grades[student_j]:
            grades[student_i], grades[student_j] = grades[student_j], grades[student_i]
            names[student_i], names[student_j] = names[student_j], names[student_i]

for student_idx in range(student_amount):
    print(names[student_idx], grades[student_idx])
'''
'''
a = list(map(int, input().split()))
b = 0
c = 0

for i in range(2, len(a)):
    if a[i] > a[i-1] + a[i-2]:
        b += 1
        if c < a[i]:
            c = a[i]

if b != 0:
    print(b, c)
else:
    print(0, 0)
'''

'''
a = list(map(int, input().split()))

print(*a, sep='+', end='')
print('=' + str(sum(a)))
'''

'''
def arithmetic(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Division by zero is impossible"
    else:
        return "Unknown operation"


print(arithmetic(10, 5, '+'))
print(arithmetic(10, 5, '-'))
print(arithmetic(10, 5, '*'))
print(arithmetic(10, 5, '/'))
print(arithmetic(10, 0, '/'))
print(arithmetic(10, 5, '^'))
'''

'''
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


print(is_year_leap(2020))
print(is_year_leap(1900))
print(is_year_leap(2000))
print(is_year_leap(2021))
'''

'''
def season(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    else:
        return "Incorrect number month"


print(season(1))
print(season(4))
print(season(7))
print(season(10))
print(season(13))
'''

'''
def bank(a, years):
    for _ in range(years):
        a += a * 0.10
    return a


initial_amount = 1000
years = 5
final_amount = bank(initial_amount, years)
print(f"Amount on account in {years} years: {final_amount:.2f} $")
'''

'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(2))
print(is_prime(4))
print(is_prime(17))
print(is_prime(1000))
'''

'''
def date(day, month, year):
    try:
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False


print(date(31, 12, 2020))
print(date(31, 11, 2020))
print(date(29, 2, 2020))
print(date(29, 2, 2021))
'''

"""
def arithmetic(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Division by zero is impossible"
    else:
        return "Unknown operation"
"""
'''
def xor_cipher(string, key):
    ciphered = ''.join(chr(ord(char) ^ key) for char in string)
    return ciphered


def xor_no_cipher(ciphered_string, key):
    deciphered = ''.join(chr(ord(char) ^ key) for char in ciphered_string)
    return deciphered


original_text = "Hello, World!"
key = 123


ciphered_text = xor_cipher(original_text, key)
print("Encrypted text:", ciphered_text)


deciphered_text = xor_no_cipher(ciphered_text, key)
print("Decrypted text:", deciphered_text)
'''
'''
a = int(input())


def number_1(n):
    if n <= 1:
        return 1

    return number_1(n - 1) + number_1(n - 2)*3


print(number_1(4))
'''

'''
def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


while 1:
    try:
        x = int(input('a = '))
        y = int(input('b = '))
        print('NOK:', lcm(x, y))
    except ValueError:
        break
'''
'''
file = open("text.txt")

lines = 0
words = 0
symbols = 0

for line in file:
    lines += 1
    words += len(line.split())
    symbols += len(line)

print("Lines:", lines)
print("Words:", words)
print("Symbols:", symbols)
'''
'''
num = int(input())
base = 16
letters = '0123456789ABCDEF'
new = ''

while num > 0:
    num, remainder = divmod(num, base)
    new = letters[remainder] + new

print(new)
'''
'''
a = [randint(1, 50) for i in range(10)]
a.sort()
print(a)

value = int(input())

left = 0
right = len(a) - 1

while left <= right:
    center = (left + right) // 2
    if value == a[center]:
        print('ID =', center)
        break
    if value > a[center]:
        left = center + 1
    else:
        right = center - 1
else:
    print('No value')
'''

'''
a = input()
num_list = []

num = ''
for char in a:
    if char.isdigit():
        num = num + char
    else:
        if num != '':
            num_list.append(int(num))
            num = ''
if num != '':
    num_list.append(int(num))

print(num_list)
'''

income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    x = income - 10000
    tax_payable = x * 10 / 100
else:
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)
