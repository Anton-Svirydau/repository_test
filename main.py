# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


'''
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
'''


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