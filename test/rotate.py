import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    n = len(arr)
    d = d % n
    return arr[d:] + arr[:d]

#Example 1
d = 2
arr = [1, 2, 3, 4, 5]
print(rotateLeft(d, arr))