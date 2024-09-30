import datetime
import random
from random import randint

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
'''

'''
TOKEN = ""
CRYPTO_NAME_TO_TICKER = {
    "Bitcoin": "BTCUSDT",
    "Ethereum": "ETHUSDT",
    "Doge": "DOGEUSDT"
}


bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(row_width=3)
    for crypto_name in CRYPTO_NAME_TO_TICKER.keys():
        item_button = KeyboardButton(crypto_name)
        markup.add(item_button)
    bot.send_message(message.chat.id, "Choose a crypto", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in CRYPTO_NAME_TO_TICKER.keys())
def send_price(message):
    crypto_name = message.text
    ticker = CRYPTO_NAME_TO_TICKER[crypto_name]
    price = get_price_by_ticker(ticker=ticker)
    bot.send_message(message.chat.id, f"Price of {crypto_name} to USDT is {price}")


def get_price_by_ticker(*, ticker: str) -> float:
    endpoint = "https://api.binance.com/api/v3/ticker/price"
    params = {
        'symbol': ticker,
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    price = round(float(data["price"]), 2)
    return price


bot.infinity_polling()
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
while True:
    s = input('(+, -, *, /): ')
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        a = float(input('a = '))
        b = float(input('b = '))
        if s == '+':
            print('%.2f' % (a + b))
        elif s == '-':
            print('%.2f' % (a - b))
        elif s == '*':
            print('%.2f' % (a * b))
        elif s == '/':
            if b != 0:
                print('%.2f' % (a / b))
            else:
                print('no / 0!')
'''

'''
a = []
for i in range(10):
    n = round(random.random() * 100)
    a.append(n)
print("A =", a)

b = []
i = 0
length = len(a)
while i < length:
    if 35 < a[i] < 65:
        b.append(a[i])
        del a[i]
        length = length - 1
    else:
        i += 1

print("A =", a)
print("B =", b)
'''

a = [randint(0, 99) for j in range(10)]
print("A =", a)

b = []
i = len(a) - 1
while i >= 0:
    if 35 < a[i] < 65:
        b.insert(0, a.pop(i))
    i -= 1

print("A =", a)
print("B =", b)
