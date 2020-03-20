import argparse 

def factorial(n:int) -> int:
    if n < 2:
        return 1
    else:
        return factorial(n-1) * n

parser = argparse.ArgumentParser()
parser.add_argument('fact', help='num to be factorized', type=int)

args = parser.parse_args()

print(factorial(args.fact)))
