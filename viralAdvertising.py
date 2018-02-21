#!/bin/python3

import sys

def viralAdvertising(n):
    count =0
    j =0 
    for i in range(n):
        if i==0 :
            count+=2
            j=2
        else:
            count += int((j*3)/2)
            j = int((j*3)/2)
    return count

if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
