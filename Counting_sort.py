import math
import os
import random
import re
import sys

def countingSort(arr):
    zero_arr = [0] * 100
    for i in arr:
        zero_arr[i] += 1
    return zero_arr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
