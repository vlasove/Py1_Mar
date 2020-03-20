numbers = {1:('one', 2) , 2:"two", 9:'nine', 0:'zero'}
numbers['new_elem'] = 1293821083


for key in numbers.keys():
    print(key, '|||', numbers[key])

for val in numbers.values():
    print(val)

for key, val in numbers.items():
    print(key, val)
