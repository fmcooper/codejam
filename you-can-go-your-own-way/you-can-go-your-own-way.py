# codejam foregone solution
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da


# loop through each direction in the given path and go the 
# opposite way
def getRes(s, p):
    m = ""
    for d in p:
        if d == "E":
            m += "S"
        else:
            m += "E"
    return m


# input and output
t = int(input())
for i in range(t):
    s = int(input())
    p = list(input())
    print("Case #" + str(i+1) + ": " + str(getRes(s, p)))
