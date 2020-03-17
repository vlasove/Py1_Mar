n = int(input())
numerator = 0
denominator = 1
while n > 0:
    a = int(input())     # a/b
    b = int(input())

    numerator = numerator*b + denominator*a
    denominator = denominator * b
    n -= 1

# calc gcd ...

print(numerator//gcd, '/', denominator//gcd)


