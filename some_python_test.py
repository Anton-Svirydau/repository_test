from timeit import default_timer as timer
import random
import itertools
import os
import sys


start = timer()


some_list = [1, 2, 3, 4, 5]


some_choice = random.choice(some_list)

# print(some_choice)

randrange_some = random.randrange(1, 5, 1)

# print(randrange_some)

randint_some = random.randint(1, 5)

# print(randint_some)

sample_some = random.sample(some_list, 3)

# print(sample_some)

uniform_some = random.uniform(1, 5)

# print(uniform_some)


accumulate_sum = list(itertools.accumulate(some_list))

# print(accumulate_sum)

combinations_some = list(itertools.combinations(some_list, 2))
combinations_some_with_replacement = list(itertools.combinations_with_replacement(some_list, 2))

# print(*combinations_some)
# print(*combinations_some_with_replacement)

product_some = list(itertools.product('ABCD', 'xy'))

# print(*product_some)

starmap_some = list(itertools.starmap(pow, [(2,5), (3,2), (10,3)]))

# print(*starmap_some)

take_while_some = list(itertools.takewhile(lambda x: x<5, [1,4,6,4,1]))

# print(*take_while_some)

os_name = os.name

# print(os_name)

get_pid_some = os.getpid()

# print(get_pid_some)

get_default_encoding = sys.getdefaultencoding()

# print(get_default_encoding)

get_file_system_encoding_some = sys.getfilesystemencoding()

# print(get_file_system_encoding_some)

get_windows_version_some = sys.getwindowsversion()

# print(get_windows_version_some)

# print(sys.modules)

print(sys.platform)


end = timer()
print(f"Время выполнения: {end - start:.5f} секунд")
