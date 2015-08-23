# Function that takes a list of numbers and returns the largest.

import random

def max_in_list(numlist):
    max = numlist[0]
    for number in numlist:
        if number > max:
            max = number
    return max
            
if __name__ == "__main__":
    numlist = random.sample(range(1, 100), 6)
    print(numlist)
    print(max_in_list(numlist))