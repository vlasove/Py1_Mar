a = [1,2,3,4]
b = a
c = a.copy()
b[0] = 'kek'
c[0] = 'q'
print(a , b, c)

d = a[1:-1]
d[0] ='kasjdkasjd'
print(a,d)