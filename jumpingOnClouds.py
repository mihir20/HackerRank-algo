#!/bin/python3

import sys

def jumpingOnClouds(c, k):
    e=100
    index =0
    if c[0]==0:
        e=e-1
    else :
        e=e-3
    index = index + k
    while index%(len(c))!=0:
        if c[index]==0:
            e=e-1
        else :
            e=e-3
        index = index + k
    return e
        

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c, k)
    print(result)
