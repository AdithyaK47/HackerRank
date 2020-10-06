#!/bin/python3

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_apples = 0
    total_oranges = 0
    for i in range(0, len(apples)):
        distance = 0
        distance = a + apples[i]
        if (distance >= s and distance <= t):
            total_apples += 1
        else: 
            pass
    for i in range(0, len(oranges)):
        distance = 0
        distance = b + oranges[i]
        if (distance >= s and distance <= t):
            total_oranges += 1
        else: 
            pass   
    print(total_apples)
    print(total_oranges)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
