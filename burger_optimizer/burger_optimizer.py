# codejam burger optimizer
# https://codingcompetitions.withgoogle.com/codejamio/round/000000000005102c/0000000000050dd4

import math

def getRes(k, d):
    length = (k+1)/2
    # counts of each size of optimal value
    counts = [0] * length
    for e in d:
        counts[e] = counts[e] + 1

    # numbers go e.g. 0, 1, 2, 3, 2, 1, 0 so for even k we have two for all 0, 1, 2, 3 and for odd k we have 2 for 0, 1, 2 and one for 3.
    sum = 0
    for i in range((k+1)/2):
        if i == (k+1)/2 - 1 and k % 2 == 1:
            c, counts = getSmallest(counts)
            sum = sum + (i - c)**2
        else:
            c, counts = getSmallest(counts)
            sum = sum + (i - c)**2
            c, counts = getSmallest(counts)
            sum = sum + (i - c)**2
    return sum


def getSmallest(counts):
    for i, c in enumerate(counts):
        if not c == 0:
            counts[i] = counts[i] - 1
            return i, counts
    return -1, counts # won't happen


# input and output
t = int(input())
for i in range(t):
    k = int(input())
    d = [int(s) for s in raw_input().split()]
    print("Case #" + str(i+1) + ": " + str(getRes(k, d)))

