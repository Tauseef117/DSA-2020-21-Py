#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'longestSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestSubarray(arr):
    # Write your code here
    n,low,high=1,1,1
    if len(arr)<2:
        return len(arr)
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            low+=1
            high+=1
        elif arr[i]-1 ==arr[i-1]:
            low=high+1
            high=1
        elif arr[i]+1 == arr[i-1]:
            high=low+1
            low=1
        else:
            low=1
            high=1
        n=max(n,low,high)
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
