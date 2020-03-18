my_list = [1, 4, 3, 12, 213, 99, 'hello']
my_list[0] = "bobbbbbbbbbbbbbbbbb"
print(my_list, type(my_list))

for elem in my_list[::-1]:
    print(elem)

empty_list = [] 
empty2_list = list()

my_zeros = [0] * 10
print(my_zeros)
