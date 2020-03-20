





































def my_inifinity_args(*args): 
    print(sum(args))
    print(type(args)) 

def my_kw_args(a, b, *args, **kwargs):
    print(args)
    print(kwargs)
    print(type(kwargs))

#This function for blalalalalalalalal
def add_sqr(a:int, b:int) -> int:
    return a**2 + b**2 +2*a*b













































































































































































print()
def add_sqr(a:int, b:int) -> int:
    return a**2 + b**2 +2*a*b


print((lambda a, b: a**2 + b**2 +2*a*b)(2,3))

func_list = [add_sqr,(lambda a, b: a**2 + b**2 +2*a*b)]
print(func_list[0](2,3))

#func_list.sort(key=lambda x: (x, x+1))

a = add_sqr
b = add_sqr 

print( a != b)

def ooo(*args:int, **kwargs):
    pass


def add(a:int):
    def new_add(b:int):
        return a + b 
    return new_add

print(add(2)(3))
o = add(2)
print(o(10))
print(o(20))



def mult(a:int):
    def new_mult(b:int):
        def new_new_mult(c:int):
            def super_new_mult(d:int):
                return a*b*c*d 
            return super_new_mult
        return new_new_mult
    return new_mult

print(mult(2)(3)(4)(5) == 120)



def my_decorator(func):
    def wrapper():
        print("HELLO I'AM DECORATOR BEFORE FUNCTION")
        password = input("Enter password:")
        if password == '12345':
            func()
        else:
            print('BLOCK!')
        print('HELLO AFTER FUNCTION')
    return wrapper

@my_new_decorator
@my_decorator
def stand_alone_func():
    print('PYTHON ORIGINAL FRESH FUNC')
stand_alone_func()

