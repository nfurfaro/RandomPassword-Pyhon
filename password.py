#password generator

import string
import random

sp = string.printable
chars = list(string.strip(sp))
length = input('How long a password would you like?:')

'''
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
'''

def main():
    password = string.join(map(str, (random.sample((chars),length))))
    print(password)

if __name__ == '__main__':
    main()