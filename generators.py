import sys
# yield returns the value and pauses the function

def my_generator():
    yield 1 # first return
    yield 2 # second return
    yield 3 # third return
    
g = my_generator()

for i in g:
    print(i)
    
print("-----------------")

g = my_generator() # initalize again to reset generator
value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value)
print("-----------------")

g = my_generator() # initalize again to reset generator
print(sorted(g))

print("-----------------")
def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1
        
cd = countdown(4)
value = next(cd)
print(value)
value = next(cd)
print(value)
value = next(cd)
print(value)
value = next(cd)
print(value)


print("-----------------")
def first_n(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(first_n(10))
print(sum(first_n(10)))

print("-----------------")

def first_n_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1
        
print(sum(first_n_generator(10)))

print(sys.getsizeof(first_n(1000000)))
print(sys.getsizeof(first_n_generator(1000000))) # generator object saves a lot of memory

print("-----------------")

def fibonacci(limit):
    first, second = 0, 1
    while first < limit:
        yield first
        first, second = second, first + second
        
fib = fibonacci(100)
for i in fib:
    print(i)
    
print("-----------------")

my_generator2 = (i for i in range(1000000) if i % 2 == 0) # dictionary comprehension

print(sys.getsizeof(my_generator2))

# for i in my_generator2:
#     print(i)

# for i in my_generator2:
#     print(i) # will not print anything because my_generator2 object finished iterating

list_comprehension = [i for i in range(1000000) if i % 2 == 0]
print(sys.getsizeof(list_comprehension))