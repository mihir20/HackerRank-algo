#!/bin/python3

import sys

def utopianTree(n):
    height =1
    for j in range(n+1):
        if j%2==0 and j!=0:
            height+=1
        elif j%2!=0:
            height*=2
    return height

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        print (result)
