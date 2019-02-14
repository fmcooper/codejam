# codejam number guessing
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000000130/0000000000000523

import sys

t = int(input())
for i in range(t):
    a, b = [int(s) for s in raw_input().split()]
    n = int(input())

    fin = False
    numGuess = 0
    while (not fin) and (numGuess < n):
        halfway = int((a + b) / 2) + 1
        print(str(halfway))
        sys.stdout.flush()
        reply = raw_input()
        if reply == 'CORRECT':
            fin = True
        elif reply == 'TOO_SMALL':
            a = halfway
        elif reply == "TOO_BIG":
            b = halfway - 1



