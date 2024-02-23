#!/usr/bin/env python3
import sys

def to_base10(i, j, k):
    return 81 * (i-1) + 9*(j-1) + (k-1)+1

# Generate prefilled values from the partially completed puzzle
def prefilled_values(sud_input):
    res = ""
    count = 0        
    for x in range(1, 10):
        for y in range(1, 10):
            if sud_input[x-1][y-1] != '.':
                res += str(to_base10(x, y, int(sud_input[x-1][y-1]))) + ' 0\n' 
                count += 1
    return count, res

# Generate the clauses for the individual cells
# Constraints: Each cell contains at least one number
def individual_constraints():
    res = ""
    count = 0
    vars = 0
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                res += str(to_base10(i, j, k))+' '
                vars += 1
            count += 1
            res += '0\n' # Terminate with a 0
    return vars, count, res


# Generate the clauses for the rows
# Constraints: Each row contains each number at most once
def rows_constraints():
    count = 0
    res = ""
    for i in range(1, 10):
        for k in range(1, 10):
            for j in range(1, 9):
                for l in range(j+1, 10):
                    res+= str(-to_base10(i, j, k)) + ' ' + str(-to_base10(i, l, k)) + ' 0\n'
                    count += 1
    return count, res

# Generate the clauses for the columns
# Constraints: Each column contains each number at most once
def columns_constraints():
    count = 0
    res = ""
    for j in range(1, 10):
        for k in range(1, 10):
            for i in range(1, 9):
                for l in range(i+1, 10):
                    res+=str(-to_base10(i, j, k)) + ' ' + str(-to_base10(l, j, k)) + ' 0\n'
                    count += 1
    return count, res

# Generate the clauses for the mini-grids
# Constraints: Each mini-grid contains each number at most once
def mini_grid_constraints():
    count = 0
    res = ""
    for k in range(1,10):
        for a in range(0,3):
            for b in range(0,3):
                
                for u in range(1,4):
                    for v in range(1,3):
                        for w in range(v+1,4):
                            res+=str(-to_base10(3*a+u, 3*b+v, k)) + ' ' + str(-to_base10(3*a+u, 3*b+w, k)) + ' 0\n'
                            count += 1
                
                for u in range(1,3):
                    for v in range(1,4):
                        for w in range(u+1,4):
                            for t in range(1,4):
                                res+=str(-to_base10(3*a+u, 3*b+v, k)) + ' ' + str(-to_base10(3*a+w, 3*b+t, k)) + ' 0\n'
                                count += 1
    return count, res

def sud2sat():
    # Read in the input file, also removing whitespace, to get the sudoku puzzle 2D array
    sud_input = ''.join(sys.stdin.read().split())
    sud_input = sud_input.replace('0', '.').replace('*', '.').replace('?', '.')
    # Back to rows
    sud_input = [sud_input[i:i+9] for i in range(0, len(sud_input), 9)]
    
    number_of_clauses = 0
    final_res = ""
    variables = 0
    
    count, res = prefilled_values(sud_input)
    number_of_clauses += count
    final_res += res
    
    variables, count, res = individual_constraints()
    number_of_clauses += count
    final_res += res

    count, res = rows_constraints()
    number_of_clauses += count
    final_res += res
    
    count, res = columns_constraints()
    number_of_clauses += count
    final_res += res
    
    count, res = mini_grid_constraints()
    number_of_clauses += count
    final_res += res
    
    print("p cnf " + str(variables) + " " + str(number_of_clauses))
    print(final_res)
    


if __name__ == "__main__":
    sud2sat()
