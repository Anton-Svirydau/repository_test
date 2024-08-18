# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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
