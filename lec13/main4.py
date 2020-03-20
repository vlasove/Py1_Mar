import argparse 

def factorial(n:int) -> int:
    if n < 2:
        return 1
    else:
        return factorial(n-1) * n

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbosity', help='display calculus', action="store_true")
args = parser.parse_args()
if args.verbosity:
    for i in range(0, 100):
        print('Factorial of', i, 'is', factorial(i))
else:
    print(factorial(99))