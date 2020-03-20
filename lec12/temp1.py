fhandler = open('input2.txt', 'r')

print(fhandler)
#print(fhandler.read()[::-1])

for line in fhandler.readlines():
    line = line.strip()
    print(line)

print(fhandler.read()[::-1])
fhandler.close()

