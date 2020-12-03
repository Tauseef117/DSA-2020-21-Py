import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    a = 0
    while (i < (len(c) - 1)):
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
            a += 1
        else:
            i += 1
            a += 1
    return a


if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)
