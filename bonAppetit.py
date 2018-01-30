#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    total = sum(ar)
    if b == total/2:
        return int(ar[k]/2)
    else:
        return 'Bon Appetit'

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
