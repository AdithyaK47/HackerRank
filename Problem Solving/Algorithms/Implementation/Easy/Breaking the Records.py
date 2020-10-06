#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    highest = scores[0]
    lowest = scores[0]
    maxCount = 0
    minCount = 0
    finalList = []
    for i in range(0, len(scores)):
        if scores[i] > highest:
            maxCount += 1
            highest = scores[i]
        try: 
            if scores[i+1] < lowest :
                minCount += 1
                lowest = scores[i+1]
        except:
            break
    finalList.append(maxCount)
    finalList.append(minCount)
    return finalList
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
