#!/bin/python3

import sys
def reverse (x):
    y=0
    while (x!=0):
        y *= 10
        y+=x%10
        x= int(x/10)
    return y
        

def beautifulDays(i, j, k):
    count =0
    for a in range(i,j+1):
        if (abs(a-reverse(a)))%k == 0 :
            count+=1
    return count

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)
