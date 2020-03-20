# .json --- Java Script Object Notation
"""
{
    "firstName" : "Bob",
    "lastName" : "Grog",
    "age" : 24,
    "features" : {
        "iq": -200,
        "isLazy" : 1
    }
}
"""

import json 
import csv

data = {
    'name' : 'Bob', 
    'age' : None
}

with open('data.json', 'w') as js_file:
    json.dump(data, js_file, indent=4)

with open('data.json', 'r') as js_file:
    data_new = json.load(js_file)
    print(data_new)
    print(type(data_new))

q = json.dumps(data)

print(q)
