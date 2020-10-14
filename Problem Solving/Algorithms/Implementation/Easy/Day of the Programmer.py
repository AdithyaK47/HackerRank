#!/bin/python3

import math
import os
import random
import re
import sys

def dayOfProgrammer(year):
    if (year >= 1700 and year <= 1917):
        if (year % 4 == 0):
            answer = f'12.09.{year}'
        else:
            answer = f'13.09.{year}'
    elif (year == 1918):
        answer = f'26.09.{year}'
    else:
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            answer = f'12.09.{year}'
        else:
            answer = f'13.09.{year}'
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
