#password generator

import string
import random

sp = string.printable
chars = list(string.strip(sp))
length = int(input('How long a password would you like?:'))

def main():
  print string.join(map(str, (random.sample((chars),length))))

if __name__ == '__main__':
  main()