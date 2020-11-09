#!/bin/python3

import math
import os
import random
import re
import sys

def minimumDistances(a):
    dictionary = {}

    for i in range(0, len(a)):
        if a.count(a[i]) > 1:
            dictionary[a[i]] = [j for j in range(len(a)) if a[j] == a[i]]
        else:
            pass

    differences = []  
    for x in dictionary.values():
        differences.append([j - i for i, j in zip(x[: -1], x[1 :])])

    if not differences:
        return -1
    else:
        return "".join(list(map(str, min(differences))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
