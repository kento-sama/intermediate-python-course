# lambda input: output
from functools import reduce

add10 = lambda x: x + 10

print(add10(5))


def add10(x):
    return x + 10

print(add10(5))

multiply = lambda x, y: x * y

print(multiply(3, 7))

# sorted(iterable, [key=func])
points2d = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2d_sorted = sorted(points2d, key=lambda x: x[1])
print(points2d)
print(points2d_sorted)


def sort_by_y(x):
    return x[1]


points2d_sorted = sorted(points2d, key=sort_by_y)
print(points2d_sorted)

points2d_sorted = sorted(points2d, key=lambda x: x[0] + x[1])
print(points2d)
print(points2d_sorted)

# map(func, iterable) function
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b))

c = [x * 2 for x in a]
print(c)

# filter(func, iterable)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = filter(lambda x: x % 2 == 1, a)
print(list(b))

c = [x for x in a if x % 2 == 1]
print(c)

#reduce(func, iterable) 2nd argument passes 2 parameters to 1st argument
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = reduce(lambda x, y: x + y, a)
print(b)
