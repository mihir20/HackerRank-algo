#!/bin/python3

import sys

def solve(n, s, d, m):
    res =0
    for i in range(n-m+1):
        sum = 0
        for j in range(i,i+m):
            sum += s[j]
        if sum == d:
            res+=1
    return res

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
