def print_name(name): # parameter
    print(name)
    
print_name("Kent") # argument

def foo(a, b, c, d=4): # d is default parameter. It's optional. You can pass an argument or not.
    print(a, b, c, d)
    
foo(a=1, c=2, b=3) # keyword argument
foo(1, b=3, c=2) # positional argument first before keyword argument
# foo(1, b=3, a=2) # cannot use keyword argument that's already used by positional argument

def foo2(a, b, *args, **kwargs): # args is a tuple and kwargs is a dictionary
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
        
""" *args takes the remaining argument that has no keys as a tuple and
    **kwargs takes all the keyword arguments that does not exist as a paramater as a dictionary """
foo2(1, 2, 3, 4, 5, six=6, seven=7)
foo2(1, 2, 3, 4)


def foo3(a, b, *, c, d): # forces all parameters after * as a keyword argument 
    print(a, b, c, d)
    
foo3(1, 2, c=3, d=4)


def foo4(*args, last): # all parameters after *args must be a keyword argument
    for arg in args:
        print(arg)
    print(last)
    
foo4(1, 2, 3, last=4)


def foo5(a, b, c):
    print(a, b, c)
    
# iterable must have the same size as the parameter requried
my_list = [0, 1, 2]
foo5(*my_list) # unpacks the list to match the arguments required of the function.
my_tuple = (0, 1, 2,) # unpacks the tuple to match the arguments required of the function.
foo5(*my_tuple)
my_dict = {"a": 1, "b": 2, "c": 3}
foo5(**my_dict) # unpacks the tuple to match the arguments required of the function. Note. Keys must match the parameters


def foo6():
    global number # access global variable that can be read and written. Without global, it will create a new local variable
    x = number
    number = 3
    print("Number insde function:", x)
    
number = 0

foo6()
print(number)

def foo7(x):
    x = 5 # does not modify emmutable objects
    
    
var = 10
foo7(var)
print(var)


def foo8(a_list):
    a_list.append(4) # modifies mutable objects
    a_list[0] = 100
    a_list += [400, 500, 600]
    a_list = [100, 200, 300] # does not modify the global variable. Cannot reassign
    
    
    
my_list = [1, 2, 3]
foo8(my_list)
print(my_list)