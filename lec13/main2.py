import argparse

parser = argparse.ArgumentParser()
parser.add_argument('echo', help="this is echo argument")
parser.add_argument('-e', '--echo2', help="this is echo2 argument")
args = parser.parse_args()
print(args)
print(args.echo, args.echo2)