#!/bin/python3

import sys

def circularArrayRotation(a, m, k):
    c=[]
    for i in m:
        if i-k >= 0 :
            c.append(a[i-k])
        else :
            c.append(a[len(a)+i-k])
    return c

if __name__ == "__main__":
    n, k, q = input().strip().split(' ')
    n, k, q = [int(n), int(k), int(q)]
    a = list(map(int, input().strip().split(' ')))
    m = []
    m_i = 0
    for m_i in range(q):
       m_t = int(input().strip())
       m.append(m_t)
    result = circularArrayRotation(a, m, k)
    print ("\n".join(map(str, result)))