# i = 20  # Переменная цикла
# while i < 10: # Условие цикла
#     print(i) # Тело цикла
#     i += 2 # Изменение переменной цикла


message = input() # Переменная цикла
while message != "": # Условие цикла
    print(message) # Тело цикла
    message = input() # Изменение переменной цикла


n! = n * (n - 1) * (n - 2) * .... * 1

n = int(input()) # Переменная цикла
answer = 1

while n > 1: # Условие цикла
    answer = answer * n   # Тело цикла
    n -= 1 # Изменение переменной цикла

print(answer)