#!/bin/python3

import math
import os
import random
import re
import sys


def beautifulDays(i, j, k):
    days = 0
    for day in range(i, j + 1):
        temp = str(day)[::-1]
        difference = abs(day - int(temp))
        if (difference % k == 0):
            days += 1
        else:
            pass
    return days
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
