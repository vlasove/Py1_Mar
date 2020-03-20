# a - int, b - int, c - int
def average(a:int ,b:int ,c:int) -> int:
    return a + b + c / 3

print(average(1,2,3)) 


def new_average( a:int ,b:int = 0,c:int = 0) -> int:
    return a + b + c // 3

print(new_average(1))
print(new_average(1,c=2))
print(new_average(1,2,3))






a = '2;3' -> [2,3]
b = '3;4'-> [3,4]
res_a = [int(t) for t in a.split(';')]
x1 = res_a[0]
y1 = res_a[1]