squares = []
for i in range(1, 51):
    if i % 2 == 0:
        squares.append( i ** 2)
    else:
        squares.append( i ** 3)
print(squares[:10])

new_squares = [ i ** 2 if i % 2 == 0  else i ** 3 for i in range(1 ,51) ]