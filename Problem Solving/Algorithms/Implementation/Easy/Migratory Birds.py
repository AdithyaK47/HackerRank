#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    dictionary = {}
    for i in range(0, len(arr)):
        if arr[i] not in dictionary:
            dictionary[arr[i]] = 1
        else:
            dictionary[arr[i]] += 1

    maximum = max(list(dictionary.values()))
    requiredDict = {k:v for k, v in dictionary.items() if v == maximum}

    return min(requiredDict.keys())

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
