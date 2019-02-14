# codejam cruise control
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000000130/0000000000000524


def findSpeed(d, h):
    # for each horse, calc when they would have got to d
    # find the worst performing
    longestTime = 0.0
    for i in range(len(h)):
        distleft = d - h[i][0]
        speed = h[i][1]
        time = float(distleft) / float(speed)
        if time > longestTime:
            longestTime = time
    return float(d) / longestTime



# input and output
t = int(input())
for i in range(t):
    d,n = [int(s) for s in raw_input().split()]
    
    h = []
    for j in range(n):
        k,s = [int(s) for s in raw_input().split()]
        h.append((k,s))

    print("Case #" + str(i+1) + ": " + str(findSpeed(d, h)))