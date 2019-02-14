# codejam senate evacuation
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000000130/00000000000004c0

# return results string
def getRes(t, n, p):
    res = "Case #" + str(t) + ": "
    fin = False
    total = sum(p)

    # loop over the parties, removing one from the largest each time. Stop when we only have 2 parties left
    while n > 2:
        largest = p[0]
        largestIndex = 0
        fin = True
        for ind in range(len(p)): 
            if p[ind] > 0:
                fin = False
            if (p[ind] > largest):
                largest = p[ind]
                largestIndex = ind
        p[largestIndex] = p[largestIndex] - 1
        if p[largestIndex] == 0:
            n = n - 1
        total = total - 1
        res = res + chr(ord('A') + largestIndex) + " "

    # when there are only two partes left then equalise their numbers and then take them out one from each every time
    if n == 2:
        nonzero = [i for i, e in enumerate(p) if e != 0]
        fin = False
        while not fin:
            if p[nonzero[0]] > p[nonzero[1]]:
                res = res + chr(ord('A') + nonzero[0]) + " "
                p[nonzero[0]] = p[nonzero[0]] - 1
            elif p[nonzero[1]] > p[nonzero[0]]:
                res = res + chr(ord('A') + nonzero[1]) + " "
                p[nonzero[1]] = p[nonzero[1]] - 1
            else:
                res = res + chr(ord('A') + nonzero[0]) + chr(ord('A') + nonzero[1]) + " "
                p[nonzero[0]] = p[nonzero[0]] - 1
                p[nonzero[1]] = p[nonzero[1]] - 1
            if p[nonzero[0]] == 0 and p[nonzero[1]] == 0:
                fin = True;
    return res
   
    
# input and output
t = int(input())
for i in range(t):
    n = int(input())
    p = [int(s) for s in raw_input().split()]
    print(getRes(i+1, n, p))
