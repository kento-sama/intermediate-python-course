mydict = {"name": "Kent", "age": 28, "city": "Iligan"}
print(mydict)

mydict2 = dict(name="Mary", age="27", city="Iligan")
print(mydict2)

print(mydict["name"])
print(mydict["age"])
print(mydict["city"])

mydict["email"] = "kentharvey.pecorro92@gmail.com"

print(mydict)
print(mydict["email"])

del mydict["email"]
print(mydict)

if "name" in mydict:
    print(mydict["name"])

if "lastname" in mydict:
    print(mydict["lastname"])

try:
    print(mydict["lastname"])
except KeyError:
    print("'lastname' key does not exist")

for key in mydict:
    print(key)

for key in mydict.keys():
    print(key)

for i in mydict:
    print(mydict[i])

for values in mydict.values():
    print(values)

mydict_copy = mydict
print(mydict)
print(mydict_copy)
mydict_copy["email"] = "kentharvey.pecorro92@gmail.com"
print(mydict)

mydict2_copy = dict(mydict2)
mydict2_copy["email"] = "test@email.com"
print(mydict2)
print(mydict2_copy)

# merge and change values of existing keys
mydict.update(mydict2)
print(mydict)

data = [('sravan', 23), ('ojaswi', 15),
        ('rohith', 8), ('gnanesh', 4), ('bobby', 20)]

data_to_dict = dict([(key, value) for key, value in data])
print(data_to_dict)
