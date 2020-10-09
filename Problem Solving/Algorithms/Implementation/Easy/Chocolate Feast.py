#!/bin/python3

import math
import os
import random
import re
import sys


def chocolateFeast(n, c, m):
    initial_count = n/c
    if (initial_count - m < 0):
        return int(initial_count)
    elif (initial_count - m == 0):
        return int(initial_count) + 1
    else:
        wrapper = initial_count
        while(wrapper >= m):
            wrapper -= m
            initial_count += 1
            wrapper += 1
        return int(initial_count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
