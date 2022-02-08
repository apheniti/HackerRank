#Input Format
#A single line containing a positive integer, .

#Constraints
#0<n<100

#Output Format
#Print Weird if the number is weird. Otherwise, print Not Weird.

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if(n&1==1 or 6<=n<=20): print('Weird');
    else: print('Not Weird');
