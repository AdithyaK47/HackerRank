#!/bin/python3

import math
import os
import random
import re
import sys

def twoStrings(s1, s2):
    list_s1 = []
    list_s2 = []
    list_s1[:0] = s1
    list_s2[:0] = s2

    n = len(set(list_s1))
    if (len(set(list_s1) - set(list_s2)) != n):
        return "YES"
    else:
        return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
