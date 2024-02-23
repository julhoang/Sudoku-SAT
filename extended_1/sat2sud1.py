#!/usr/bin/env python3
import sys

# Convert decimal number to base 9, return i, j, k
def get_val(num):
    return ((num - 1) % 9) + 1

def sat2sud():
    sat_input = sys.stdin.read().split('\n')
    
    if("UNSAT" == sat_input[0]):
        print("Problem is unsatisfiable.")
    else:
        nums = [int(x) for x in sat_input[1].split() if int(x) >= 0]
        
        for r in range(81):
            count = 0
            for c in range(81):
                count+=1
                location = nums[r*81+c]
                k = (location - 1) % 81 + 1
                
                if count % 3 == 0 & count != 81:
                    print(k, end=' ')
                else :
                    print(k, end='')
            print()
                

if __name__ == "__main__":
    sat2sud()