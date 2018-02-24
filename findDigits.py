#!/bin/python3

import sys

def findDigits(n):
    number = n
    count =0
    while n != 0:
        i =n%10
        if i!=0 and number%i==0:
            count+=1
        n = int(n/10)
    return count
            

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)
