m = (str(int(i) ** 2)  for i in input().split() if str(int(i) ** 2)[-1] != '9')
print(' '.join(m))

