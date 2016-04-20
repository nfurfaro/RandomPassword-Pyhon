# password generator

import string
import random

chars = (str.strip(string.printable))
length = input('How long a password would you like?:')
rndm_sample = random.sample((chars), length)


def main():
    print(''.join(map(str, rndm_sample)))

if __name__ == '__main__':
    main()

    """
todo:
   - try to replace ''string" module functionality with standard builtin str
    - validate input - ensure positive integer (natural?)
    - check output, make sure it contains at least one of each:
        Upper/lower case letter, number, symbol
        how to implement...if statement, looping or try?

    """
