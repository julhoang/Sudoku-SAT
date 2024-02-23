#!/usr/bin/env python3
import sys
import math

def to_base10(i, j, k):
    return 81 * (i-1) + 9*(j-1) + (k-1)+1

# Generate prefilled values
def prefilled_values(sud_input, n):
    res = ""
    count = 0      
    for x in range(1, n+1):
        for y in range(1, n+1):
            if sud_input[x-1][y-1] != '.':
                res += str(to_base10(x, y, int(sud_input[x-1][y-1]))) + ' 0\n' 
                count += 1
    return count, res

# Generate the clauses for the individual cells
# Constraints: Each cell contains at least one number
def individual_constraints(n):
    res = ""
    count = 0
    vars = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, 10):
                res += str(to_base10(i, j, k))+' '
                vars +=1
            count += 1
            res += '0\n' # Terminate with a 0
    return vars, count, res


# Generate the clauses for the rows
# Constraints: Each row contains each number at most once
def rows_constraints(n):
    count = 0
    res = ""
    for i in range(1, n+1):
        for k in range(1, 10):
            for j in range(1, n):
                for l in range(j+1, n+1):
                    res+= str(-to_base10(i, j, k)) + ' ' + str(-to_base10(i, l, k)) + ' 0\n'
                    count += 1
    return count, res

# Generate the clauses for the columns
# Constraints: Each column contains each number at most once
def columns_constraints(n):
    count = 0
    res = ""
    for j in range(1, n+1):
        for k in range(1, 10):
            for i in range(1, n):
                for l in range(i+1, n+1):
                    res+=str(-to_base10(i, j, k)) + ' ' + str(-to_base10(l, j, k)) + ' 0\n'
                    count += 1
    return count, res

# Generate the clauses for the mini-grids
# Constraints: Each mini-grid contains each number at most once
def mini_grid_constraints(n):
    count = 0
    res = ""
    sqrt = int(math.sqrt(n))
    
    for k in range(1,10):
        for a in range(0,sqrt):
            for b in range(0,sqrt):
                
                for u in range(1,sqrt+1):
                    for v in range(1,sqrt):
                        for w in range(v+1,sqrt+1):
                            res+=str(-to_base10(sqrt*a+u, sqrt*b+v, k)) + ' ' + str(-to_base10(sqrt*a+u, sqrt*b+w, k)) + ' 0\n'
                            count += 1
                
                for u in range(1,sqrt):
                    for v in range(1,sqrt+1):
                        for w in range(u+1,sqrt+1):
                            for t in range(1,sqrt+1):
                                res+=str(-to_base10(sqrt*a+u, sqrt*b+v, k)) + ' ' + str(-to_base10(sqrt*a+w, sqrt*b+t, k)) + ' 0\n'
                                count += 1
    return count, res

def sud2sat():
    # Read in the input file, also removing whitespace, to get the sudoku puzzle 2D array
    input_str = sys.stdin.read().split()
    n = len(input_str[0])
    
    sud_input = ''.join(input_str)
    sud_input = sud_input.replace('0', '.').replace('*', '.').replace('?', '.')
    
    # Back to rows
    sud_input = [sud_input[i:i+81] for i in range(0, len(sud_input), n)]
    
    prefilled_count, prefilled_res = prefilled_values(sud_input, n)
    variables, individual_count, individual_res = individual_constraints(n)
    row_count, row_res = rows_constraints(n)
    col_count, col_res = columns_constraints(n)
    grid_count, grid_res = mini_grid_constraints(n)
    
    number_of_clauses = prefilled_count + individual_count + row_count + col_count + grid_count
    
    print("p cnf " + str(variables) + " " + str(number_of_clauses))
    print(prefilled_res)
    print(individual_res)
    print(col_res)
    print(row_res)
    print(grid_res)


if __name__ == "__main__":
    sud2sat()
