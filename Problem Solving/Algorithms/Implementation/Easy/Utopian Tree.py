#!/bin/python3

import math
import os
import random
import re
import sys

def utopianTree(n):
    treeHeight = 1
    if n == 0:
        return treeHeight
    elif n % 2 == 0:
        i = 0
        while(i < n/2):
            treeHeight = treeHeight*2 + 1
            i += 1
        return treeHeight
    else:
        i = 0
        while(i < (n-1)/2):
            treeHeight = treeHeight*2 + 1
            i += 1
        return treeHeight*2           



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
