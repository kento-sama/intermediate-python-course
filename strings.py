from timeit import default_timer as timer
my_string = "Hello world"
print(my_string)
multiple_line = """Hello \
world \
string"""

print(multiple_line)
print(my_string[0])
print(my_string[1:5])
print(my_string[-1])
print(my_string[::2])
print(my_string[::-1])

greeting = "Hello"
name = "Kent"
sentence = greeting + " " + name
print(sentence)
sentence = f"{greeting} {name}"
print(sentence)

for letter in greeting:
    print(letter)

if "y" in greeting:
    print("exists")
else:
    print("not exists")

my_string = "    Hello world     "
my_string = my_string.strip() # strip functions trims the string white spaces
print(my_string)
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith("Hel"))
print(my_string.endswith("rld"))

print(my_string.find("o")) # returns the index of the substring given. -1 if not found
print(my_string.index("o")) # like find but returns error if not found

print(my_string.count("l"))

print(my_string.replace("world", "Kent")) # does not modify the original string

my_string = "how are you doing?"
my_list = my_string.split()
print(my_list)

new_string = ",".join(my_list) # combines the list into 1 whole string with the given object string in between
print(new_string)

my_list = ["a"] * 6
start = timer()
my_string = ""
for i in my_list:
    my_string += i # uses a lot of memory
end = timer()
print(f"start: {start} end: {end} duration: {end - start}") # slower

start = timer()
my_string = "".join(my_list)
end = timer()
print(f"start: {start} end: {end} duration: {end - start}") # faster

var = "Kent"
my_string = "the variable is %s" % var # %d integer %.f for float
print(my_string)

my_string = "the variable is {v}".format(v=var)
print(my_string)

my_string = f"the variable is {var}"
print(my_string)