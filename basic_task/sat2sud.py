#!/usr/bin/env python3
import sys

def sat2sud():
    sat_input = sys.stdin.read().split('\n')
    
    if("UNSAT" == sat_input[0]):
        print("Problem is unsatisfiable.")
    else:
        nums = [int(x) for x in sat_input[1].split() if int(x) > 0]
        
        # Go through every row
        for r in range(9):
            count = 0

            # Go through every column
            for c in range(9):
                count+=1

                # Iterate through each variable and extract the value
                location = nums[r*9+c]
                k = (location - 1) % 9 + 1
                
                # Formatting
                if count % 3 == 0 & count != 9:
                    print(k, end=' ')
                else :
                    print(k, end='')
            print()
                

if __name__ == "__main__":
    sat2sud()