a,b,c = int(input()), int(input()), int(input())

if a >= b and a >= c:
    if b >= c:
        print(a,b,c) 
    else:
        print(a,c,b)
elif b >= a and b >= c:
    .....