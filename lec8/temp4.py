def factorial(n):
    if n == 1 or n == 0:
        return 1 
    else:
        return factorial(n - 1) * n

for i in range(1, 1000):
    print('Factorial:', i, 'is', factorial(i))