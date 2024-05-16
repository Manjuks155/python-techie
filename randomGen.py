import random

# a <= x <= b
rand_num = random.randint(0, 2)

# a <= x < b
rand_num = random.randrange(0, 2)

# to generate floating point number between 0 and 1
rand_num = random.random()

# to generate the floating point number in the range
rand_num = random.uniform(1, 2)

list_n = [10, 4, -5, 25, 18, 2]
rand_num = random.choice(list_n)

print(rand_num)

