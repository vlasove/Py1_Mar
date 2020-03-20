fname = input()

try:
    fhandler = open(fname, 'r')
except FileNotFoundError as f_err:
    print('Exception during file opening:', f_err)
    fhandler = open('input.txt', 'r')

print(fhandler.read())
fhandler.close()
