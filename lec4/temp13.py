h = int(input())

for i in range(h):
    spaces = ' ' * (h - i - 1)
    dogs = '@' *( 2 * i + 1)
    print(spaces + dogs)