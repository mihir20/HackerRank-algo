#!/bin/python3

import sys

def greaterOF( a, b ):
    if a>b:
        return a
    else:
        return b

def catAndMouse(x, y, z):
    ac = greaterOF(x-z,z-x)
    bc = greaterOF(y-z,z-y)

    if ac == bc :
        return "Mouse C"
    elif ac > bc:
        return "Cat B"
    else:
        return "Cat A"

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print ("".join(map(str, result)))


