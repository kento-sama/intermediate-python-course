# does not allow duplicate
my_set = {1, 2, 3, 4, 5, 1, 2, 3}
print(my_set)

my_list = [1, 2, 3, 4, 5]
print(set(my_list))

# sets is unordered
my_string = "Hello World"
print(set(my_string))

my_set = {}
print(type(my_set))
my_set = set()
print(type(my_set))

my_set.add(1)
my_set.add(2)
my_set.add(3)

print(my_set)
my_set.remove(2)

print(my_set)

# my_set.remove(4) # error because the item to be removed does not exist
my_set.discard(4) # remove if exists. Do nothing if item does not exist
print(my_set)

removed_item = my_set.pop()
print(removed_item)
print(my_set)

my_set.add(1)
my_set.add(2)

for i in my_set:
    print(i)

if 1 in my_set:
    print("exists")
else:
    print("does not exist")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)
i = odds.intersection(evens)
print(i)
i = odds.intersection(primes)
print(i)
i = evens.intersection(primes)
print(i)

set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_b = {1, 2, 3, 10, 11, 12}

diff = set_a.difference(set_b) # set_a - set_b
print(diff)
diff = set_b.difference(set_a)
print(diff) # set_b - set_a

diff = set_a.symmetric_difference(set_b) # prints all items except the similar items from different sets
print(diff)

set_a.update(set_b) # combine 2 sets to set_a
print(set_a)

set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_a.intersection_update(set_b) # intersects set_a and set_b and assign to set_a
print(set_a)

set_a = {1, 2, 3, 4, 5, 6}
set_b = {1, 2, 3}
print(set_a.issubset(set_b))
print(set_b.issubset(set_a))
print(set_a.issuperset(set_b)) # opposite of subset
print(set_b.issuperset(set_a))

set_b = set_a
print(set_b)
set_b.add(7)
print(set_a)
set_b = set(set_a) # or set_a.copy()
print(set_b)

a = frozenset([1, 2, 3, 4, 5]) # I don't know it's purpose
print(a)
