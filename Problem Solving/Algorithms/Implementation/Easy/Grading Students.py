#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    addOne = [4,9]
    addTwo = [3,8]
    for i in range(0, len(grades)):
        if grades[i] < 38:
            pass             
        else:
            if grades[i]%10 in addOne:
                grades[i]+=1
            elif grades[i]%10 in addTwo:
                grades[i]+=2
            else:
                pass
    return grades
        
                 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
