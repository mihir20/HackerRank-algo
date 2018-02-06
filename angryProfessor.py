#!/bin/python3

import sys

def angryProfessor(k, a):
    atd = 0
    for i in a:
        if i <= 0:
            atd+=1
    if atd < k:
        return 'YES'
    else :
        return 'NO'

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = list(map(int, input().strip().split(' ')))
        result = angryProfessor(k, a)
        print(result)
