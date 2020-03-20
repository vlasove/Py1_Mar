message = 'Hello world!'
long_message = "Hi there! Obi Van K E N O B E E"
dictionary = {} # letter : count 
for letter in long_message.split():
    if letter in dictionary.keys():
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1

print(dictionary)

