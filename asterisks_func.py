result = 5 * 7
print(result)

result = 5 ** 7
print(result)

zeroes = [0, 1] * 10
print(zeroes)

zeroes = (0, 1) * 10
print(zeroes)

mult_str = "AB" * 10
print(mult_str)

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
        
foo(1, 2, 3, 4, 5, d="d", e="e", c="c")

numbers = [1, 2, 3, 4, 5, 6]
beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)

my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

new_list = [*my_tuple, *my_list, *my_set] # merges iterables into 1 list
print(new_list)

dict_a = {"a": 1, "b": 2}
dict_b = {"c": 3, "d": 4}
my_dict = {**dict_a, **dict_b} # merges a dictionary
print(my_dict)