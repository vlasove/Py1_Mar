lhs = 150
rhs = 190

max_h = -1
min_h = 300

persons = 0

message = input() # Переменная цикла
while message != '!': # Условие
    value = int(message)
    if value >= lhs and value <= rhs:
        persons += 1
        if value >= max_h:
            max_h = value 
        if value <= min_h:
            min_h = value
    message = input() # Изменение переменной цикла
    
print(persons)
print(min_h, max_h)