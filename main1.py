import datetime

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

"""
def selection_sort(self, unsorted, n):
  
  for i in range(0, n):

    current_min = unsorted[i]

    min_index = i

    for j in range(i, n):

      if unsorted[j] < current_min:
        current_min = unsorted[j]
        min_index = j

    swap(unsorted, i, min_index)
"""

"""
def bubble_sort(self, unsorted, n):
    for i in range(0, n - 1):

        swapped = False

    for j in range(0, n - 1 - i):

        if unsorted[j].value > unsorted[j + 1].value:
            swap(unsorted, j, j + 1)
            swapped = True
"""


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


utc_time = datetime.datetime.now(datetime.UTC)
print(utc_time)

current_datetime = datetime.datetime.now()
print(current_datetime)
print(current_datetime.isoformat())
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)

some_datetime = datetime.datetime(year=2021, month=5, day=1, hour=12, minute=30, second=15, microsecond=123456)
print(some_datetime)

current_date = datetime.date.today()
print(current_date)

current_datetime = datetime.datetime.now()
current_date = current_datetime.date()
print(current_date)


day_ago = current_datetime - datetime.timedelta(days=1)
print(day_ago)


current_datetime = datetime.datetime.now()
current_datetime.strftime("%A, %d %B %Y")

isoformat = "2023-08-07T20:15:30.384294"
my_datetime = datetime.datetime.fromisoformat(isoformat)
print(type(my_datetime))
print(my_datetime)