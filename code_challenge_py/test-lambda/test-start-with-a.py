def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

map_object = map(starts_with_A, fruit)
print(list(map_object))

map_object = map(lambda s: s[0] == "A", fruit)
print(list(map_object))

map_object = filter(lambda s: s[0] == "A", fruit)
print(list(map_object))

######################
from functools import reduce

def add(x, y):
    return x + y

list = [2, 4, 7, 3]
print(reduce(add, list))

print(reduce(lambda x,y:x+y,list))
