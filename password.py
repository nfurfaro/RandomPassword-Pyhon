# password generator

import random

chars = list(map(chr, range(33, 127)))
length = input('How long a password would you like?:')
rand_sample = random.sample((chars), length)


def main():
    print(''.join(map(str, rand_sample)))

if __name__ == '__main__':
    main()

    """
todo:
    - validate input - ensure positive integer (natural?)
    - check output, make sure it contains at least one of each:
        Upper/lower case letter, number, symbol
        how to implement...if statement, looping?

    """
