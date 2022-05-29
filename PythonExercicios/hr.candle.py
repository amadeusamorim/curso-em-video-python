#!/bin/python3

import os

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    temp = candles[0]
    c = 0
    for i in range(1, len(candles)):
        if candles[i] > temp:
            temp = candles[i]
    for i in range(0, len(candles)): 
        if candles[i] == temp:
            c += 1
    return c


birthdayCakeCandles([3, 9, 6 , 5])