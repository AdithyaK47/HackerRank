#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            positive_count += 1
        elif arr[i] < 0:
            negative_count += 1
        else:
            zero_count += 1
    print("{:.6f}".format(positive_count/len(arr)))
    print("{:.6f}".format(negative_count/len(arr)))
    print("{:.6f}".format(zero_count/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
