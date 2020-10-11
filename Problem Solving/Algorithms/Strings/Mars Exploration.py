#!/bin/python3

import math
import os
import random
import re
import sys


def marsExploration(s):
    number_of_msgs = len(s)/3
    expected_msg = 'SOS' * int(number_of_msgs)
    total = 0

    for i in range(0, len(s)):
        if(i % 3 == 1):
            if (s[i] != 'O'):
                total += 1
            else:
                pass
        else:
                if (s[i] != 'S'):
                    total += 1
                else:
                    pass
    
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
