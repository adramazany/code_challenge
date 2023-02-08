import json

f = open('hw1-data.json')
data = json.load(f)
print(data)
print(data['L'])
print(data['dcutsq'])
print(data['rho'])
