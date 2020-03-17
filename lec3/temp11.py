my_set = set([1,2,3])
print(len(my_set))

for i in my_set:
    print(i)

if 10 in my_set:
    print("OK")

my_set.add(10)

my_set.discard(2)
q = my_set.pop()

my_set.clear()

