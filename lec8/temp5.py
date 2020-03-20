def quarter(x,y):
    if x > 0 and y > 0 :
        print('I asdas')
    elif x < 0 and y > 0:
        print('II')
    elif x < 0 and y < 0:
        print('III')
    else:
        print('IV')





def equation(pair1, pair2):
    x1 ,y1 = (float(t) for t in  pair1.split(';')) # ['1', '2']
    x2 ,y2 = (float(t) for t in  pair2.split(';'))
    if x2 == x1:
        print()
    elif y2 = y1:
        print()
    else:
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1 























def average(a,b,c,d,e):
    avg = (a + b + c + d + e) / 5
    print(avg)
    return avg 


print(average(1,2,3,4,5))

A = [1,2,3,454,-1]
print(A.sort())
print(A)