#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    jump = 0
    i = 0

    while(i < len(c) - 1):

      if (i == (len(c) - 2) and c[i] != 1):
        jump += 1
        i += 1
      elif (c[i + 1] == 0 and c[i + 2] == 0):
        jump += 1
        i += 2
      elif (c[i + 1] == 1 and c[i + 2] == 0):
        jump += 1
        i += 2
      elif (c[i + 1] == 0 and c[i + 2] == 1):
        jump += 1
        i += 1   

    return (jump)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
