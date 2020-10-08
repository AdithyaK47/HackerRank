#!/bin/python3

import math
import os
import random
import re
import sys

def angryProfessor(k, a):
    early_total = 0
    for i in range(0, len(a)):
        if (a[i] <= 0):
            early_total += 1
        else:
            pass
    if early_total >= k:
        return "NO"
    else:
        return "YES"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
