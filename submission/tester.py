#!/usr/bin/env python3

import re
import os

def main():
    filestr = """Grid 01
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
Grid 02
200080300
060070084
030500209
000105408
000000000
402706000
301007040
720040060
004010003
Grid 03
000000907
000420180
000705026
100904000
050000040
000507009
920108000
034059000
507000000
Grid 04
030050040
008010500
460000012
070502080
000603000
040109030
250000098
001020600
080060020
Grid 05
020810740
700003100
090002805
009040087
400208003
160030200
302700060
005600008
076051090
Grid 06
100920000
524010000
000000070
050008102
000000000
402700090
060000000
000030945
000071006
Grid 07
043080250
600000000
000001094
900004070
000608000
010200003
820500000
000000005
034090710
Grid 08
480006902
002008001
900370060
840010200
003704100
001060049
020085007
700900600
609200018
Grid 09
000900002
050123400
030000160
908000000
070000090
000000205
091000050
007439020
400007000
Grid 10
001900003
900700160
030005007
050000009
004302600
200000070
600100030
042007006
500006800
Grid 11
000125400
008400000
420800000
030000095
060902010
510000060
000003049
000007200
001298000
Grid 12
062340750
100005600
570000040
000094800
400000006
005830000
030000091
006400007
059083260
Grid 13
300000000
005009000
200504000
020000700
160000058
704310600
000890100
000067080
000005437
Grid 14
630000000
000500008
005674000
000020000
003401020
000000345
000007004
080300902
947100080
Grid 15
000020040
008035000
000070602
031046970
200000000
000501203
049000730
000000010
800004000
Grid 16
361025900
080960010
400000057
008000471
000603000
259000800
740000005
020018060
005470329
Grid 17
050807020
600010090
702540006
070020301
504000908
103080070
900076205
060090003
080103040
Grid 18
080005000
000003457
000070809
060400903
007010500
408007020
901020000
842300000
000100080
Grid 19
003502900
000040000
106000305
900251008
070408030
800763001
308000104
000020000
005104800
Grid 20
000000000
009805100
051907420
290401065
000000000
140508093
026709580
005103600
000000000
Grid 21
020030090
000907000
900208005
004806500
607000208
003102900
800605007
000309000
030020050
Grid 22
005000006
070009020
000500107
804150000
000803000
000092805
907006000
030400010
200000600
Grid 23
040000050
001943600
009000300
600050002
103000506
800020007
005000200
002436700
030000040
Grid 24
004000000
000030002
390700080
400009001
209801307
600200008
010008053
900040000
000000800
Grid 25
360020089
000361000
000000000
803000602
400603007
607000108
000000000
000418000
970030014
Grid 26
500400060
009000800
640020000
000001008
208000501
700500000
000090084
003000600
060003002
Grid 27
007256400
400000005
010030060
000508000
008060200
000107000
030070090
200000004
006312700
Grid 28
000000000
079050180
800000007
007306800
450708096
003502700
700000005
016030420
000000000
Grid 29
030000080
009000500
007509200
700105008
020090030
900402001
004207100
002000800
070000090
Grid 30
200170603
050000100
000006079
000040700
000801000
009050000
310400000
005000060
906037002
Grid 31
000000080
800701040
040020030
374000900
000030000
005000321
010060050
050802006
080000000
Grid 32
000000085
000210009
960080100
500800016
000000000
890006007
009070052
300054000
480000000
Grid 33
608070502
050608070
002000300
500090006
040302050
800050003
005000200
010704090
409060701
Grid 34
050010040
107000602
000905000
208030501
040070020
901080406
000401000
304000709
020060010
Grid 35
053000790
009753400
100000002
090080010
000907000
080030070
500000003
007641200
061000940
Grid 36
006080300
049070250
000405000
600317004
007000800
100826009
000702000
075040190
003090600
Grid 37
005080700
700204005
320000084
060105040
008000500
070803010
450000091
600508007
003010600
Grid 38
000900800
128006400
070800060
800430007
500000009
600079008
090004010
003600284
001007000
Grid 39
000080000
270000054
095000810
009806400
020403060
006905100
017000620
460000038
000090000
Grid 40
000602000
400050001
085010620
038206710
000000000
019407350
026040530
900020007
000809000
Grid 41
000900002
050123400
030000160
908000000
070000090
000000205
091000050
007439020
400007000
Grid 42
380000000
000400785
009020300
060090000
800302009
000040070
001070500
495006000
000000092
Grid 43
000158000
002060800
030000040
027030510
000000000
046080790
050000080
004070100
000325000
Grid 44
010500200
900001000
002008030
500030007
008000500
600080004
040100700
000700006
003004050
Grid 45
080000040
000469000
400000007
005904600
070608030
008502100
900000005
000781000
060000010
Grid 46
904200007
010000000
000706500
000800090
020904060
040002000
001607000
000000030
300005702
Grid 47
000700800
006000031
040002000
024070000
010030080
000060290
000800070
860000500
002006000
Grid 48
001007090
590080001
030000080
000005800
050060020
004100000
080000030
100020079
020700400
Grid 49
000003017
015009008
060000000
100007000
009000200
000500004
000000020
500600340
340200000
Grid 50
300200000
000107000
706030500
070009080
900020004
010800050
009040301
000702000
000008006"""

    # Grab each sudoku puzzle
    pattern = re.compile(r'Grid \d\d\n([\d\s]+)')
    matches = pattern.findall(filestr)


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


    # Go through each sudoku
    for grid in matches:
        # Write the current puzzle into file, then call our programs and minisat
        puz_text = open("puzzle.txt", "w")
        puz_text.write(grid)
        puz_text.close()
        os.system('./sud2sat.py <puzzle.txt >puzzle.cnf')
        os.system('minisat puzzle.cnf assign.txt >stat.txt')
        os.system('./sat2sud.py <assign.txt >solution.txt')
        sol_text = open("solution.txt", "r")
        #print(sol_text.read())
        sol_text.close()


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