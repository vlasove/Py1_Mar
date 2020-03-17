A = int(input())
B = int(input())
C = int(input())

if A == 0:
    if B != 0:
        x = -C/B
        print(x)
    else:
        print()
else:
    D = B ** 2 - 4*A*C  
    if D > 0: 
        X1 = (-B + D**(0.5))/(2*A)
        X2 = (-B - D**(0.5))/(2*A)
        if X1 < X2:
            print(X1)
            print(X2)
        else:
            print(X2)
            print(X1)
    elif D == 0:
        X = -B/(2 * A)
        print(X)
    else:
        print()
