max_value = -10**10
min_value = 10**10

n = int(input())
while n > 0:
    number = int(input())
    if number > max_value:
        max_value = number 
    if number < min_value:
        min_value = numer
    n -= 1

print("Maximum is: ", max_value)