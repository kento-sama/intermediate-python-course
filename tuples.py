import sys
import timeit

mytuple = ("banana", "cherry", "apple")

print("original tuple: %s" % str(mytuple))

mylist = ["banana", "cherry", "apple"]
mytuple = tuple(mylist)
print("Tuple form list: %s" % str(mytuple))

print(mytuple[2])
print(len(mytuple))

# To be continued

if "banana" in mylist:
    print("yes")
else:
    print("no")

apple_tuple = ('a', 'p', 'p', 'l', 'e')

print(apple_tuple)
print(apple_tuple.count('p'))
print(apple_tuple.index('l'))

apple_list = list(apple_tuple)
print(apple_list)

number_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(number_tuple[1::2])
num_first, *num_mid, num_last = number_tuple
print(num_first)
print(num_mid)
print(num_last)

banana, cherry, apple = mytuple
print(banana)
print(cherry)
print(apple)


number_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list is larger than tuple despite having the same content
print(sys.getsizeof(number_tuple), "bytes")
print(sys.getsizeof(number_list), "bytes")

# list is longer to create than tuple
print(timeit.timeit(stmt="[0, 1, 2, 3, 4 ,5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4 ,5)", number=1000000))
