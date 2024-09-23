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
'''

'''
def first_last_same(number_list):
    print("Given list:", number_list)

    first_num = number_list[0]
    last_num = number_list[-1]

    if first_num == last_num:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))
'''

'''
def palindrome(number):
    print("original number", number)
    original_num = number

    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")


palindrome(121)
palindrome(125)
'''

'''
def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


nums = [4, 5, 6, 7, 8, 9, 0]
print(nums)

shift(nums, -2)
print(nums)

shift(nums, 3)
print(nums)
'''

'''
num = int(input())
base = 16
letters = 'ABCDEF'
new = ''

while num > 0:
    num, remainder = divmod(num, base)
    if remainder > 9:
        letter_id = remainder - 10
        remainder = letters[letter_id]
    new = str(remainder) + new

print(new)
'''

'''
n, m = [int(i) for i in input().split()]
spiral = [[0] * m for _ in range(n)]
c = 1
for k in range(min(n // 2 + 1, m //2 + 1)):
    for j in range(k, m - k):
        if spiral[k][j] == 0:
            spiral[k][j] = c
            c += 1
    for i in range(1 + k, n - k):
        if spiral[i][m - k - 1] == 0:
            spiral[i][m - k - 1] = c
            c += 1
    for j in range(m - k - 2, k - 1, -1):
        if spiral[n - k - 1][j] == 0:
            spiral[n - k - 1][j] = c
            c += 1
    for i in range(n - k - 2, k, -1):
        if spiral[i][k] == 0:
            spiral[i][k] = c
            c += 1
for i in range(n):
    for j in range(m):
        print(str(spiral[i][j]).ljust(3), end=' ')
    print()
'''

'''
def lastSurvivor(n, k):
    if n == 1:
        return 1
    elif n > 1:
        return (1 + (lastSurvivor(n - 1, k) + k - 1) % n)


n, k = int(input()), int(input())
print(lastSurvivor(n, k))
'''

'''
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
if all(i in sum(matrix,[]) for i in range(1, n**2 + 1)):
    print('YES' if all(sum(i) == sum(j) == sum([matrix[i][i] for i in range(n)]) == sum([matrix[n-i-1][i] for i in range(n)]) for i in matrix for j in list(map(list, zip(*matrix)))) else 'NO')
else:
    print('NO')
'''

'''
lst = input().split()


def sub_lists(lst1):
    lists = [[]]
    for i in range(len(lst1) + 1):
        for j in range(i):
            lists.append(lst1[j:i])
    lists = sorted(lists, key=len)
    return lists


print(sub_lists(lst))
'''

'''
def del_from_tuple(tpl, elem):
    if elem in tpl:
        elem_index = tpl.index(elem)
        return tpl[:elem_index] + tpl[elem_index + 1:]
    return tpl


print(del_from_tuple((1, 2, 3), 1))
print(del_from_tuple((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(del_from_tuple((2, 4, 6, 6, 4, 2), 9))
'''

'''
BEGIN_INDEX = 0
END_INDEX = -1


def slicer(any_tuple, element):
    first = second = BEGIN_INDEX

    if element in any_tuple:
        first = any_tuple.index(element)
    if any_tuple.count(element) > 1:
        second = any_tuple.index(element, first + 1) + 1
    else:
        second = END_INDEX

    return any_tuple[first:second]


print(slicer((1, 2, 3), 8))
print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
'''

'''
from collections import namedtuple
Student = namedtuple('Student', 'name age mark city')
students = (
   Student('Elena', '13', 7.1, 'Minsk'),
   Student('Olga', '11', 7.9, 'Brest'),
   Student('Lisa', '14', 9.1, 'Pinsk'),
   Student('Dima', '12', 5.2, 'Vitebsk'),
   Student('Maksim', '15', 6.1, 'Mogilev'),
   Student('Kolya', '11', 8.7, 'Gomel'),
   Student('Artur', '13', 5.8, 'Vilnus')
)


def good_students(students):
        total_mark = 0

        for student in students:
            total_mark += student.mark
        avg_mark = total_mark / len(students)

        good_mark_students = [student.name for student in students if student.mark >= avg_mark]
        print('students ', ', '.join(good_mark_students), ' in this semester!')


good_students(students)
'''

'''
def slicer(any_tuple, element):
    if element in any_tuple:
        if any_tuple.count(element) > 1:
            first_index = any_tuple.index(element)
            second_index = any_tuple.index(element, first_index + 1) + 1
            return any_tuple[first_index:second_index]
        else:
            return any_tuple[any_tuple.index(element):]
    else:
        return ()
'''


'''
def binary_search(list, start_element, key):
    end_element = len(list) - 1
    while start_element <= end_element:
        middle_element = start_element + (end_element - start_element) // 2
        if list[middle_element] == key:
            return middle_element
        elif list[middle_element] < key:
            start_element = middle_element + 1
        else:
            end_element = middle_element - 1
    return -1


sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

find_element = 24

result = binary_search(list=sequence, start_element=0, key=find_element)
print(result)
'''

'''
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return "No item in list"


my_list = [1, 3, 5, 7, 9, 11, 13, 14, 15, 17, 19, 21]

result_1 = binary_search(my_list, 17)
result_2 = binary_search(my_list, 12)
print(result_1)
print(result_2)
'''

'''
def sort_by_len(element: str) -> int:
    return len(element)


sort_by_len_lambda = lambda element: len(element)
print(sort_by_len("banana"))
print(sort_by_len_lambda("banana"))


fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits, key=lambda element: len(element))

fruits = ["apple", "banana", "cherry", "date"]
longest_word = max(fruits, key=lambda x: len(x))
print(longest_word)
'''

'''
def is_even(n):
    return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = list(filter(is_even, numbers))
print(filtered_numbers)


def is_adult(person):
    return person['age'] >= 18


people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 40}
]
filtered_people = list(filter(is_adult, people))
print(filtered_people)
'''

'''
def insertion_sort(unsorted, n):
    for i in range(1, n):
        val = unsorted[i].value
        hole = i
        while hole > 0 and unsorted[hole - 1].value > val:
            unsorted[hole].value = unsorted[hole - 1].value
            hole -= 1
        unsorted[hole].value = val
'''

'''
def divide(self, unsorted, lower, upper):
    if upper <= lower:
        return
    mid = (lower + upper) // 2
    divide(unsorted, lower, mid)
    divide(unsorted, mid + 1, upper)
    merge(unsorted, lower, mid, mid + 1, upper)


def merge(unsorted, l_lower, l_upper, r_lower, r_upper):
    i, j = l_lower, r_lower
    temp = []
    while i <= l_upper and j <= r_upper:
        if unsorted[i].value <= unsorted[j].value:
            temp.append(unsorted[i])
            i += 1
        else:
            temp.append(unsorted[j])
            j += 1
    while i <= l_upper:
        temp.append(unsorted[i])
        i += 1
    while j <= r_upper:
        temp.append(unsorted[j])
        j += 1
    for y, k in enumerate(range(l_lower, r_upper + 1)):
        unsorted[k] = temp[y]
'''

'''
def quick_sort(self, unsorted, start, end):
    if start >= end:
        return
    i_pivot = partition(unsorted, start, end - 1)
    quick_sort(unsorted, start, i_pivot)
    quick_sort(unsorted, i_pivot + 1, end)


def partition(self, unsorted, start, end):
    pivot = unsorted[end]
    i_pivot = start
    for i in range(start, end):
        if unsorted[i].value <= pivot.value:
            swap(unsorted, i, i_pivot)
            i_pivot += 1
    swap(unsorted, i_pivot, end)
    return i_pivot
'''


def bubble_sort(self, unsorted, n):
    for i in range(0, n - 1):

        swapped = False
        for j in range(0, n - 1 - i):
            if unsorted[j].value > unsorted[j + 1].value:
                swap(unsorted, j, j + 1)
                swapped = True
        if not swapped:
            break
