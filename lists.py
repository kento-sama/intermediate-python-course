mylist = ["banana", "cherry", "apple"]
print(mylist)

for i in mylist:
    print(i)

if "cherry" in mylist:
    print("Yes")
else:
    print("No")

print("length: %d" % len(mylist))

mylist.append("lemon")

print(mylist)

mylist.insert(2, "blueberry")

print(mylist)

print("temporary reversed: %s" % str(mylist[::-1]))
mylist.reverse()
print("permanently reversed: %s" % str(mylist))

new_list = sorted(mylist)

print("permanently sorted new list: %s" % str(new_list))
print("original list: %s" % str(mylist))

mylist.sort()
print("permanently sorted original list: %s" % str(mylist))

print("added list: %s " % str(new_list + mylist))

fruit = mylist.pop()
print(fruit)
print(mylist)

mylist.remove("cherry")
print(mylist)

mylist.clear()
print(mylist)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("number lists: %s" % str(num_list))
print("num_list[1: 5] %s " % str(num_list[1: 5]))

print(num_list[1::2])

squared_list = [i * i for i in num_list]
print("squared list: %s" % str(squared_list))

original_list = ["banana", "cherry", "apple"]
copy_list = original_list[::] # or you can use the .copy() or list() function

print("original list: %s" % str(original_list))
print("copy list: %s" % str(copy_list))