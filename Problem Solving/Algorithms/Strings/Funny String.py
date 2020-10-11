#!/bin/python3

import math
import os
import random
import re
import sys


def funnyString(s):
    string_list = []
    for i in range(0, len(s)):
        string_list.append(ord(s[i])) 
    reverse_list = string_list[::-1]

    diff_string = []
    diff_revString = []

    for x, y in zip(string_list[0::], string_list[1::]):
        diff_string.append(abs(y-x))
    for x, y in zip(reverse_list[0::], reverse_list[1::]):
        diff_revString.append(abs(y-x))

    if(diff_string == diff_revString):
        return 'Funny'
    else:
        return 'Not Funny'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
