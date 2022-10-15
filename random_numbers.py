import random

r = random.random() # 0 - 0.999 ...
print(r)

r = random.random() * 100 # 0 - 99.999...
print(int(r)) # cast to make it 0 - 99

r = random.uniform(1, 10) # random float numbers from 1 - 10
print(r)

r = random.randint(1, 10) # random integer from 1 - 10
print(r)

r = random.randrange(1, 10) # random integer from 1 - 9
print(r)

r = random.normalvariate(0, 1) # random value from a normal distribution. arg1 mean, arg2 standard deviation
print(r)

my_list = list('ABCDEFGHIJKL')
print(my_list)
r = random.choice(my_list) # pick random choice from a sequence or list
print(r)

r = random.sample(my_list, 3) # pick a number of random choices from a sequence or list (unique)
print(r)

numbers = range(10)
r = random.choices(numbers, k=3) # pic a number of random choices from a sequence or list (can be repeated)
print(r)

random.shuffle(my_list) # shuffle and modify the list itself
print(my_list)

# Reproduce random data
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

import secrets # used for security. Will generate a true random number and not reproduceable. Cons: take longer time
s = secrets.randbelow(10) # random number from 0 to n - 1
print(s)

s = secrets.randbits(4) # random number with n number of bits (see binary numbers). Ex. 4 bits 0000 - 1111 (0-15)
print(s)

my_list = list('ABCDEFGHIJKL')
s = secrets.choice(my_list) # random choice from a list
print(s)

# pip install numpy
import numpy as np
a = np.random.rand(3, 3) # generate random number in an array 0 - 0.99999.... Ex. 3 x 3 array
print(a)

a = np.random.randint(0,10, (3, 4)) # generate a random array from [arg1, arg2) with size arg3 which is an int or a tuple for multiple dimensions.
print(a)

a = np.array([[6, 5, 6, 2], [0, 4, 0, 9], [7, 8, 4, 4]])
print(a)
np.random.shuffle(a) # shuffles the outer array
print(a)

# Reproduceable
np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))
