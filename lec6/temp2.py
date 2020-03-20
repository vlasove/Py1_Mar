numbers = {1:('one', 2) , 2:"two", 9:'nine', 0:'zero'}



print(numbers[0], numbers[9])

words = {'one' : 1, 3:2, 123123.1231: 3, None:0, (1,2,3) : 100, True: 200}
print(words[(1,2,3)], words[None])

d = dict()
d1 = {}

print(words)
# Keys:
1) Уникальные
2) Неизменямые (базовые типы + кортеж)
3) Словарь - разупорядоченная коллекция (основана на множестве)