a = set([1,2,3,4])
b = set([3,4,5,6,7])


c = a.union(b) # a U b
print('Union:', c)
d  = a.intersection(b)
print('Intersection:', d)
e = a - b # a.difference(b) 
print('Difference a-b:', e)
f = a ^ b # a.symmetric_difference(b)
print("Symmetric difference a^b:", f)
