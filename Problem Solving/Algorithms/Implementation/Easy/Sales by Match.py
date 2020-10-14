#!/bin/python3

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    pair = 0
    colors = set(ar)
    counts = []

    for color in colors:
        counts.append(ar.count(color))
    
    for i in counts:
        if (i >= 2):
            pair += int(i/2)
        else:
            pass
    
    return pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
