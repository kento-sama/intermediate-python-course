from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

a = "aaabbbbccccc"
my_counter = Counter(a)
print(my_counter)
for key, value in my_counter.items():
    print(key)
    print(value)
    print(key * value)

print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements())) # list all items individually
print(list(a)) # list all characters in a string individually

point = namedtuple("point", 'x,y')
pt = point(1, -4)
print(pt)
print(pt.x)
print(pt.y)

ordered = OrderedDict()
ordered["b"] = 2
ordered["c"] = 3
ordered["d"] = 4
ordered["a"] = 1

print(ordered)

d = defaultdict(int) # print the default empty value of specific data type if the key does not exist. Example 0 for int, 0.0 for float, [] for list
d["a"] = 1
d["b"] = 2
d["c"] = 3
d["d"] = 4

print(d["b"])
print(d["e"]) # print out 0

d = deque()
d.append(1)
d.append(2)
d.append(3)
print(d)

d.appendleft(4)
d.appendleft(5)
d.appendleft(6)
print(d)

popped = d.pop()
print(popped)
print(d)

left_popped = d.popleft()
print(left_popped)
print(d)

d.extend([3, 7])
print(d)
d.extendleft([4, 8])
print(d)
d.rotate(-3) # < 0 rotate to the left. > 0 rotate to the right
print(d)

d.clear()
print(d)

