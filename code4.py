#!/bin/python3

#(1500,2700) both included and divisible by 7 && multiple of 5!!

for x in range(1500,2700+1):
    if x%5==0 and x%7==0:
        print(x,end=' ')
print('\n')
