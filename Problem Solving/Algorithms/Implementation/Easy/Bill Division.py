#!/bin/python3

import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    total = 0
    for i in range(0, len(bill)):
        total += bill[i]
    
    actualCost = (total - bill[k])/2
    
    if (b!=actualCost):
        print(int(b - actualCost))
    else:
        print('Bon Appetit')


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
