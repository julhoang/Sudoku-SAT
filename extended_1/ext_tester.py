#!/usr/bin/env python3

import re
import os

def main():
    # stat.txt statistics worst and average case
    worst_num_vars = 0
    worst_num_clauses = 0
    worst_parse_time = 0
    worst_eliminated_clauses = 0
    worst_simplification_time = 0
    worst_restarts = 0
    worst_conflicts = 0
    worst_decisions = 0
    worst_propagations = 0
    worst_conflict_literals = 0
    worst_memory_used = 0
    worst_cpu_time = 0

    avr_num_vars = 0
    avr_num_clauses = 0
    avr_parse_time = 0
    avr_eliminated_clauses = 0
    avr_simplification_time = 0
    avr_restarts = 0
    avr_conflicts = 0
    avr_decisions = 0
    avr_propagations = 0
    avr_conflict_literals = 0
    avr_memory_used = 0
    avr_cpu_time = 0

    count = 0


    # Regex for statistics
    pattern_num_vars = re.compile(r'Number of variables:\s*(\d*)')
    pattern_num_clauses = re.compile(r'Number of clauses:\s*(\d*)')
    pattern_parse_time = re.compile(r'Parse time:\s*(\d*.\d*)')
    pattern_eliminated_clauses = re.compile(r'Eliminated clauses:\s*(\d*.\d*)')
    pattern_simplification_time = re.compile(r'Simplification time:\s*(\d*.\d*)')
    pattern_restarts = re.compile(r'restarts\s*: (\d*)')
    pattern_conflicts = re.compile(r'conflicts\s*: (\d*)')
    pattern_decisions = re.compile(r'decisions\s*: (\d*)')
    pattern_propagations = re.compile(r'propagations\s*: (\d*)')
    pattern_conflict_literals = re.compile(r'conflict literals\s*: (\d*)')
    pattern_memory_used = re.compile(r'Memory used\s*: (\d*.\d*)')
    pattern_cpu_time = re.compile(r'CPU time\s*: (\d*.\d*)')

    os.system('./sud2sat1.py <puzzle.txt >puzzle.cnf')


    os.system('minisat puzzle.cnf assign.txt >stat.txt')
    # os.system('./sat2sud.py <assign.txt >solution.txt')
    # sol_text = open("solution.txt", "r")
    # print(sol_text.read())
    # sol_text.close()


    # Grab statistics
    count += 1
    stat_txt = open("stat.txt", "r")
    curr_stats = stat_txt.read()
    stat_txt.close()

    num_vars = pattern_num_vars.search(curr_stats)
    num_clauses = pattern_num_clauses.search(curr_stats)
    parse_time = pattern_parse_time.search(curr_stats)
    eliminated_clauses = pattern_eliminated_clauses.search(curr_stats)
    simplification_time = pattern_simplification_time.search(curr_stats)
    restarts = pattern_restarts.search(curr_stats)
    conflicts = pattern_conflicts.search(curr_stats)
    decisions = pattern_decisions.search(curr_stats)
    propagations = pattern_propagations.search(curr_stats)
    conflict_literals = pattern_conflict_literals.search(curr_stats)
    memory_used = pattern_memory_used.search(curr_stats)
    cpu_time = pattern_cpu_time.search(curr_stats)

    if num_vars:
        x = int(num_vars.group(1))
        if x > worst_num_vars:
            worst_num_vars = x
        avr_num_vars += x

    if num_clauses:
        x = int(num_clauses.group(1))
        if x > worst_num_clauses:
            worst_num_clauses = x
        avr_num_clauses += x

    if parse_time:
        x = float(parse_time.group(1))
        if x > worst_parse_time:
            worst_parse_time = x
        avr_parse_time += x

    if eliminated_clauses:
        x = float(eliminated_clauses.group(1))
        if x > worst_eliminated_clauses:
            worst_eliminated_clauses = x
        avr_eliminated_clauses += x

    if simplification_time:
        x = float(simplification_time.group(1))
        if x > worst_simplification_time:
            worst_simplification_time = x
        avr_simplification_time += x

    if restarts:
        x = int(restarts.group(1))
        if x > worst_restarts:
            worst_restarts = x
        avr_restarts += x

    if conflicts:
        x = int(conflicts.group(1))
        if x > worst_conflicts:
            worst_conflicts = x
        avr_conflicts += x

    if decisions:
        x = int(decisions.group(1))
        if x > worst_decisions:
            worst_decisions = x
        avr_decisions += x

    if propagations:
        x = int(propagations.group(1))
        if x > worst_propagations:
            worst_propagations = x
        avr_propagations += x

    if conflict_literals:
        x = int(conflict_literals.group(1))
        if x > worst_conflict_literals:
            worst_conflict_literals = x
        avr_conflict_literals += x

    if memory_used:
        x = float(memory_used.group(1))
        if x > worst_memory_used:
            worst_memory_used = x
        avr_memory_used += x

    if cpu_time:
        x = float(cpu_time.group(1))
        if x > worst_cpu_time:
            worst_cpu_time = x
        avr_cpu_time += x
    
    print("WORST CASES:\n", worst_num_vars, "\t", 
        worst_num_clauses, "\t", 
        worst_parse_time, "\t", 
        worst_eliminated_clauses, "\t", 
        worst_simplification_time, "\t", 
        worst_restarts, "\t", 
        worst_conflicts, "\t", 
        worst_decisions, "\t", 
        worst_propagations, "\t", 
        worst_conflict_literals, "\t", 
        worst_memory_used, "\t", 
        worst_cpu_time,
        "\nAVERAGE CASES:\n",
        avr_num_vars / count, "\t", 
        avr_num_clauses / count, "\t", 
        avr_parse_time / count, "\t", 
        avr_eliminated_clauses / count, "\t", 
        avr_simplification_time / count, "\t", 
        avr_restarts / count, "\t", 
        avr_conflicts / count, "\t", 
        avr_decisions / count, "\t", 
        avr_propagations / count, "\t", 
        avr_conflict_literals / count, "\t", 
        avr_memory_used / count, "\t", 
        avr_cpu_time / count)



if __name__ == "__main__":
    main()