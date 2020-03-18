city = set()

for _ in range(int(input())):
    city.add(input())

new_city = input()
if new_city in city:
    print('TRY ANOTHER')
else:
    print('OK')


