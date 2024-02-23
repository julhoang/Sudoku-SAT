Submission for Project 1

This repository contains 4 folders:
- basic_task
- extended1
- extended2
- extended3

To run the code, use the following command:
```
cd <basic_task / extended1 / extended2 / extended3>
./sud2sat.py <puzzle.txt >puzzle.cnf
minisat puzzle.cnf assign.txt >stat.txt
./sat2sud.py <assign.txt >solution.txt
```

basic_task - minimal encoding of a 9x9 sudokus
- Read in an encoded puzzle and output the CNF form
- Ready to be input into minisat

extended1 - minimal encoding of ninety-five 9x9 sudokus
Read in 9 9x9 sudokus and 

extended2 - efficient encoding of a 9x9 sudokus

extended3 - extended encoding of a 9x9 sudokus


Names:
Julia Hoang - V00974641
Sara Subedi - V00986656
Angus Bews - V00980317