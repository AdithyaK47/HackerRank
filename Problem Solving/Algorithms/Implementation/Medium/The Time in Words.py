#!/bin/python3

import math
import os
import random
import re
import sys

def timeInWords(h, m):
    num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven' , 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    string = ""
    tens = ['twenty', 'thirty', 'forty', 'fifty']
    fix = ['ten', 'twenty','thirty','forty','fifty']

    if (m == 0):
        string += f"{num[h - 1]} o' clock"
    
    else:
        ten = m//10
        unit = m%10
        if (0 < m and m < 30):
            if (m == 15):
                string += f"quarter past {num[h - 1]}"
            elif (unit != 0):
                if(ten == 0 or ten == 1):
                    if (unit != 1):
                        string += f"{num[m - 1]} minutes past {num[h - 1]}"
                    else:
                        string += f"{num[m - 1]} minute past {num[h - 1]}"
                else:
                    string +=f"{tens[ten - 2]} {num[unit - 1]} minutes past {num[h - 1]}"
            else:
                string += f"{fix[ten - 1]} minutes past {num[h - 1]}"
        else:
            n = 60 - m
            ten1 = n//10
            unit1 = n%10
            
            if (m == 30):
                string += f"half past {num[h - 1]}" 
            elif (m == 45):
                string += f"quarter to {num[h]}"
            elif(unit1 != 0):
                if(ten1 == 0 or ten1 == 1):
                    string += f"{num[n - 1]} minutes to {num[h]}"
                else:
                    string +=f"{tens[ten1 - 2]} {num[unit1 - 1]} minutes to {num[h]}"
            else:
                string += f"{fix[ten1 - 1]} minutes to {num[h]}"
     

    return string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
