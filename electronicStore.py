#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    if min(keyboards)+min(drives) > s:
        return -1
    else:
        keyboards.sort()
        drives.sort()

        cost = []

        for i in keyboards:
            for j in drives:
                cost.append(i+j)
        cost.sort(reverse=True)

        for l in cost:
            if l <= s:
                return l
                

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
