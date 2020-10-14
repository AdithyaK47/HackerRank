#!/bin/python3

import os
import sys

def pageCount(n, p):
    if (n % 2 == 0):
        total_Frontturn = n/2
    else:
        total_Frontturn = (n-1)/2
    
    if (p % 2 == 0):
        front_turn = p/2
    else:
        front_turn = (p-1)/2
    
    back_turn = total_Frontturn - front_turn

    return int(min(front_turn, back_turn))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
