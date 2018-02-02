#!/bin/python3

import sys

def countingValleys(n, s):
    count = 0
    height = 0
    for h in s:
        if h == 'D':
            height-=1
        if h == 'U':
            height+=1 
            if height == 0:
                count+=1
    return count
        

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)
