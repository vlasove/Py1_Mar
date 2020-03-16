age = int(input())

if age <= 14:
    print("Access denied")
elif age > 14 and age <= 18:
    print("Demo access")
elif age > 18 and age <= 21:
    print('Demo + commenting access!')
else:
    print("Full access!")




