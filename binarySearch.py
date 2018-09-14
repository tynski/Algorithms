# Binary Search input is list of numbers (array) 
# and looking value (target). Output is guessed value
# if exist (guess) and how many iteration it takes 
# (guess_count) 

import math

def binarySearch(array, target):
    if not array:
        return None
    guess_count = 0
    n = len(array)
    Min = 0
    Max = n-1
    while Min<=Max:
        guess = math.floor((Max+Min)/2)
        guess_count += 1
        if array[guess] == target:
            return guess, guess_count
        elif array[guess] < target:
            Min = guess + 1
        else:
            Max = guess - 1
    return -1, guess_count