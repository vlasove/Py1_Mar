message = input()

for i in range(len(message)):
    if i == len(message) - 1:
        print(ord(message[i]))
    else:
        print(ord(message[i]), end=', ')