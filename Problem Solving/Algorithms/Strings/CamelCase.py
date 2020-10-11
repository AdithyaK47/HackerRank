#!/bin/python3

import math
import os
import random
import re
import sys


def camelcase(s):
    total = 1
    if (len(s) == 1):
        return total
    else:
        for i in range(0, len(s)):
            if(s[i].isupper() == True):
                total += 1
            else:
                pass
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
