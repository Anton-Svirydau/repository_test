""""""
import requests

import random
from math_operations import add
from math_operations import subtract as sub

my_int = 1
my_list = [1, 2, 3]

print(random.choice(my_list))
print(dir(random))
print(globals().keys())

print(add(1, 2))
print(sub(2, 1))
