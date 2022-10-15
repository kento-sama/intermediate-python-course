import copy

org = 5
cpy = org # creates a new variable with same reference
cpy = 6 # reassigns the variable to a new reference
print(org)
print(cpy)


org = [0, 1, 2, 3, 4] # creates a list with new reference
cpy = org # copies the reference to cpy
cpy[0] = 100 # modify value of the reference key at index 0
print(org)
print(cpy)

org1 = [0, 1, 2, 3, 4]
# shallow coppies
# cpy1 = copy.copy(org1)
# cpy1 = org1.copy()
# cpy1 = list(org1)
cpy1 = org[:]
cpy1[0] = 100
print(org1)
print(cpy1)

org2 = [[1, 2, 3, 4],[5, 6, 7, 8]]
cpy2 = copy.copy(org2)
cpy2[0][1] = 100
print(org2)
print(cpy2) # the same value on the second level because this is just a shallow copy

org3 = [[1, 2, 3, 4],[5, 6, 7, 8]]
cpy3 = copy.deepcopy(org3)
cpy3[0][1] = 100
print(org3)
print(cpy3)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee
        
p1 = Person("Kent", 29)
# p2 = p1 # copies the reference only to p2
p2 = copy.copy(p1) # shallow copy

p2.age = 18
print(p1.age)
print(p2.age)

p3 = Person("Kent", 29)
p4 = Person("Angel", 18)

company = Company(p3, p4)
# company_cpy = copy.copy(company) # shallow copy
company_cpy = copy.deepcopy(company) # deep copy

company_cpy.boss.age = company_cpy.boss.age + 1

print(company.boss.age)
print(company_cpy.boss.age)
