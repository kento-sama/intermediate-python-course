from doctest import Example
from email.policy import default
import json


# converting python object to json or serialization or encoding
person = {"name": "Mary", "age": 27, "city": "Iligan City", "hasChildren": False, "titles": ["engineer", "programmer"]}

person_json = json.dumps(person, indent=4, sort_keys=True) # converts the dictionary to string

print(person_json)

with open("person.json", mode="w") as person_file:
    #person_file.write(person_json)
    json.dump(person, person_file, indent=4, sort_keys=True) # converts the dictionary and write to json
    
# converting json to python object or deserialization or decoding
with open('example.json', mode="r") as example_file:
    example_dict = json.load(example_file) # loads a json file and convert to dictionary
print(type(example_dict))

example_json = json.dumps(example_dict, indent=4)
print(example_json)


#########################

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        


user = User("Kent", 29)


def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object passed is not an instance of User")


userJson = json.dumps(user, default=encode_user, indent=4)

print(userJson)

from json import JSONEncoder


class UserEncoder(JSONEncoder):
    
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return super().default(o)
    

userJson = json.dumps(user, cls=UserEncoder, indent=4)

print(userJson)

userJson = json.dumps(UserEncoder().default(user), indent=4) # dict to string

print(userJson)

user = json.loads(userJson) # string to dict
print(type(user))

#user = User("Kent", 29)

def decode_user(dct):
    if isinstance(dct, dict):
        return User(name=dct["name"], age=dct["age"])       
    return dct
    
user_o = decode_user(user)

print(user_o.name)
print(user_o.age)
print(isinstance(user, dict))

user_o = json.loads(userJson, object_hook=decode_user)
print(type(user_o))
print(user_o.name)
print(user_o.age)