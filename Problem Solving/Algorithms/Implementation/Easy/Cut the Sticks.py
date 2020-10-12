#!/bin/python3

import math
import os
import random
import re
import sys


def cutTheSticks(arr):
    arr.sort()
    prev = -1
    length = len(arr)
    length_list = []

    for i in arr:
        if (i != prev):
            length_list.append(length)
        length -= 1
        prev = i
    
    return length_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
