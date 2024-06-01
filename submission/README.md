# Submission for Project 1

## Names:
Julia Hoang
Sara Subedi 
Angus Bews

This repository contains 4 folders:
- basic_task: minimal encoding of a 9x9 sudokus
    1. sud2sat.py
    2. sat2sat.py
    3. tester.py
- extended1: minimal encoding of ninety-five 9x9 sudokus
    1. sud2sat1.py
    2. sat2sat1.py
- extended2: efficient encoding of a 9x9 sudokus
    1. sud2sat2.py
    2. sat2sat2.py
- extended3: extended encoding of a 9x9 sudokus
    1. sud2sat3.py
    2. sat2sat3.py

To run the code, use the following commands:
```
cd <basic_task / extended1 / extended2 / extended3>
./sud2sat.py <puzzle.txt >puzzle.cnf
minisat puzzle.cnf assign.txt >stat.txt
./sat2sud.py <assign.txt >solution.txt
```
