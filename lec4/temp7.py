city1 = input()
city2 = input()

while True:
    if city1[-1] == city2[0]:
        city1 = city2 
        city2 = input()
        continue
    else:
        print(city2)
        break
