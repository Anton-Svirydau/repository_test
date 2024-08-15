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
