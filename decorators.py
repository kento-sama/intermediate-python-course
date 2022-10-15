from distutils.log import debug
import functools

#decorator syntax
# def decorator_func(func):
#     @functools.wraps(func)
#     def wrapper(**args, **kwargs):
#         # do something here
#         result = func(*args, **kwargs) # execute the function
#         # do something here
#         return result
#     
#     return wrapper

    
def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
        
    return wrapper

@start_end_decorator # if print_name function is called, it calls the start_end_decorator function with print_name as the argument passed and returns the wrapper function
def print_name(): # this becomes the wrapper function when called
    print("Kent")
    
# print_name = start_end_decorator(print_name) # returns the wrapper of start_end_decorator function

print_name()


def start_end_decorator2(func):
    @functools.wraps(func) # preserves the identity of the func parameter
    def wrapper(*args, **kwargs):
        print("Start") # do something before executing the function
        result = func(*args, **kwargs) # execute the function
        print("End") # do something after executing the function
        return result # returns the result of the function executed
        
    return wrapper

@start_end_decorator2
def add_five(x): # this becomes the wrapper function
    return x + 5

result = add_five(10)
print(result)

print(help(add_five))
print(add_five.__name__)

def repeat(num_times): # decorator that will receive the decorator parameter
    def decorator_repeat(func): # decorator that will receive the greet function
        @functools.wraps(func) # prevents the function that uses the decorator to become the wrapper function
        def wrapper(*args, **kwargs): # this becomes the greet function but will modifications on how it will be executed
            for _ in range(num_times):
                result = func(*args, **kwargs) # this executes before assigning to result variable which is None
            
            return result # I think this is unnecessary
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}")
    
greet("Kent")


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper
        


@debug # gets called first with say_hello as argument
@start_end_decorator2 # get called second with say_hello as argment
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting

print("-------------")

say_hello("Kent")

print("-------------")

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs): # gets executed when class object is executed as a function or Class can be executed as a function
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)



@CountCalls
def say_hello2():
    print("Hello")
    
    
say_hello2()
say_hello2()
say_hello2()
say_hello2()