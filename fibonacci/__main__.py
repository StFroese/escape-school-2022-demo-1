from argparse import ArgumentParser
from . import fibonacci

parser = ArgumentParser()
parser.add_argument('n', type=int)

def main():
    args = parser.parse_args()
    print(fibonacci(args.n))


if __name__ == '__main__':
    main()