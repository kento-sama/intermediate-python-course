import operator
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement as cwr
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat

a = [1, 2]
b = [3, 4]
prod = product(a, b) # [(1, 3), (1, 4), (2, 3), (2, 4)]
print(list(prod))
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
prod = product(a, b, c)
listed_prod = list(prod)
# print(listed_prod)
print(len(listed_prod))

b = [3]
prod = product(a, b, repeat=2) # ???
print(list(prod))

a = [0, 1, 2, 3]
perm = permutations(a, 3)
listed_perm = list(perm)
print(listed_perm)
print(len(listed_perm))


comb = combinations(a, 3)
listed_comb = list(comb)
print(listed_comb)
print(len(listed_comb))
comb_wr = cwr(a, 3)
listed_cwr = list(comb_wr)
print(listed_cwr)
print(len(listed_cwr))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
acc = accumulate(a) # add as it iterate the list
listed_acc = list(acc)
print(listed_acc)

acc = accumulate(a, func=operator.mul)
listed_acc = list(acc)
print(listed_acc)


a = [0, 2, 4, 6, 7, 8, 9, 10, 1, 3, 5]
grouped = groupby(a, key=lambda i : i % 2 == 0)
for key, value in grouped:
    print(key, list(value))

for i in count(10): # create a counter starting from the parameter given
    print(i)
    if i == 20:
        break


a = [1, 2, 3]
b = 10
counter = 0
for i in cycle(a): # cycle through the list
    print(i)
    if i == 3:
        counter += 1
    if counter == 10:
        break

for i in repeat(1, 10): # repeat the given object infinitely unless indicated how many times
    print(i)