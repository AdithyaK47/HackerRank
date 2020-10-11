#!/bin/python3

import math
import os
import random
import re
import sys
import string

def pangrams(s):
    alphabets = set(string.ascii_lowercase) 
    if (set(s.lower()) >= alphabets):
      return 'pangram'
    else:
      return 'not pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
