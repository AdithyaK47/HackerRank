import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    nums = [int(x) for x in arr]
    print(sum(nums) - max(nums), sum(nums) - min(nums))
 

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
