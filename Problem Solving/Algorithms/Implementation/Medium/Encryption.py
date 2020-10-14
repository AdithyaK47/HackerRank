#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.strip()
    num = len(s)
    a = math.floor(math.sqrt(num))
    b = math.ceil(math.sqrt(num))
    list_string = []
    for i in range(b):
        list_string.append(s[i::b])
    return " ".join(list_string)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
