#!/bin/python3

import math
import os
import random
import re
import sys


def viralAdvertising(n):
    shared = 5
    liked = 2
    total = 2

    if n > 1:
        for i in range(1, n):
            shared = liked*3
            liked = math.floor(shared/2)
            total += liked
    else:
        pass

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
