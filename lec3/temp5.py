n = int(input())
loop_temp = 1
count = 0 
while loop_temp <= n:
    if n % loop_temp == 0:
        count += 1
        print(loop_temp, end=' ')
    if loop_temp == n:
        print()

    loop_temp += 1
if count == 2:
    print("ACHTUNG")