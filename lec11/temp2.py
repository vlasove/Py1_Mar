def worker(a : int):
    assert (a < 30) , 'a less then 30'
    print('COOL')

try:
    worker(5)
    print(1/1)
except AssertionError as a_err:
    print('Exception happend: ', a_err)
except ZeroDivisionError as z_err:
    print('DIVIDE BY ZERO:', z_err)
else:
    print('No errors happend')
finally:
    print('TRY/EXCEPRT BLOCK HERE')

print('AFTER TRY EXCEPT')
print('GRACEFUL SHUTDOWN')

