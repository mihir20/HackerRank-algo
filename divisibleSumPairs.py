#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    pairs =0
    for i in range(n-1):
        for j in range(i+1,n):
           sum =0
           sum = ar[i]+ar[j]
           if sum%k == 0:
              pairs+=1
    return pairs

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
