#!/bin/python3

import math
import os
import random
import re
import sys


def aVeryBigSum(ar):
    n = len(ar)
    total = 0
    for i in range(0, n):
        total+=ar[i]
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()