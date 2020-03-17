n = 2
a_set = set()
b_set = set()
while n != 0:
    message = input()
    if message == "":
        n -= 1
        continue
    if n == 2:
        a_set.add(int(message))
    if n == 1:
        b_set.add(int(message))
    
for item in a_set.intersection(b_set):
    print(item)