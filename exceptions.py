try:
    import nonexistent_module
except ModuleNotFoundError:
    print("ModuleNotFoundError")
else:
    print("Everything is fine")
finally:
    print("------------------")

try:
    a = 5 / 0
    print(a) # syntax error
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    print("Everything is fine")
finally:
    print("------------------")

try:
    a = 5 + "hello"
    print(a)
except TypeError:
    print("TypeError")
else:
    print("Everything is fine")
finally:
    print("------------------")

try:
    a = 5
    b = c
except NameError:
    print("NameError")
else:
    print("Everything is fine")
finally:
    print("------------------")

try:
    with open("test.txt", mode="r") as r:
        print(r.read())
except FileNotFoundError:
    print("FileNotFoundError")
else:
    print("Everything is fine")
finally:
    print("------------------")


try:
    a = [1, 2, 3]
    a.remove(1)
    print(a)
    a.remove(4)
except ValueError:
    print("ValueError")
    try:
        print(a[2])
    except IndexError:
        print("IndexError")
else:
    print("Everything is fine")
finally:
    print("------------------")

try:
    a = {"name": "Kent"}
    print(a["name"])
    print(a["age"])
except KeyError:
    print("KeyError")
else:
    print("Everything is fine")
finally:
    print("------------------")

user_input = 6 # input("Enter a number greater than 5: ")
print(user_input)

if int(user_input) <= 5:
    print("greater than 5")
    raise Exception("User input should be greater than 5")

x = -1
try:
    assert (x >= 0), "x is not positive"
except AssertionError as ae:
    print("AssertionError: " + str(ae))
else:
    print("Everything is fine")
finally:
    print("------------------")

try:
    a = 3 + 5
    print(a)
except TypeError:
    print("TypeError")
else:
    print("Everything is fine")
finally:
    print("------------------")


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):

    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 0:
        raise ValueTooSmallError("Value is too small", x)


try:
    test_value(-1)
except ValueTooHighError as vth:
    print(vth)
except ValueTooSmallError as vts:
    print(vts.message)
    print(vts.value)
    pass
else:
    print("Everything is fine")
finally:
    print("------------------")


