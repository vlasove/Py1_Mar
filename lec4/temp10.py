message =' ello world'

print(message[0], message[1], message[2], message[3])
print(message[0:5:2])
print(message[::-1])

for letter in message[::2]:
    print(letter)