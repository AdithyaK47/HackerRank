#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    number_string = str(n)
    numbers = list(number_string)
    numbers = [int(x) for x in numbers]
    total = 0

    for i in range(0, len(numbers)):
        if (numbers[i] == 0):
            pass
        elif (n % numbers[i] == 0):
            total += 1
        else:
            pass

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
