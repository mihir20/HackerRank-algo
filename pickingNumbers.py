#!/bin/python3

import sys

def pickingNumbers(a):
    count = 0
    entries = []
    for i in range(len(a)):
        entries.append(count)
        count =0
        for j in range(len(a)):
            if a[i] == a[j] or a[i] == a[j]+1:
                count+=1
            
    entries.sort(reverse=True)

    return max(entries)
            

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a)
    print(result)
