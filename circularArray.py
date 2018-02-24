#!/bin/python3

import sys

def circularArrayRotation(a, m, k):
    for i in range(k):
        b=a[len(a)-1]
        for j in range(len(a)-1,-1,-1):
            if j == 0:
                a[j]=b
            else :
                a[j]=a[j-1]
    c = []
    for l in m:
        c.append(a[l])
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


