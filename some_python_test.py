import random
import itertools


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
