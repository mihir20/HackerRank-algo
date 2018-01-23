#!/bin/python3

import sys

def extraLongFactorials(n):
    for i in range(1,n):
        n=n*i
    print(n)

if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)
