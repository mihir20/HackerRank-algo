#!/bin/python3

import sys

def permutationEquation(p):
    c= []
    for i in range(len(p)):
        if i+1 in p and 1+p.index(i+1) in p:
            c.append(1+p.index(1+p.index(i+1)))
    return c
        

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    result = permutationEquation(p)
    print ("\n".join(map(str, result)))


