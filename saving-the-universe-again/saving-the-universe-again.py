# codejam saving the universe again
# https://codingcompetitions.withgoogle.com/codejam/round/00000000000000cb/0000000000007966


# calculate the score of our instance
def calc_score(p):
    current_score = 0
    current_charge = 1
    for i, e in enumerate(p):
        if e == "S":
            current_score += current_charge
        else:
            current_charge = current_charge * 2
    return current_score


# swap an s down p
def swap_next_s(p):
    for i in range(len(p) - 1, -1, -1):
        
        # if we are on the first element then cannot swap
        if i == 0:
            return p, True

        # if we can swap this element with the one before then do it
        if p[i] == "S" and p[i - 1] == "C":
            temp = p[i]
            p[i] = p[i - 1]
            p[i - 1] = temp
            return p, False  

    return p, True  


# return how many swaps to resolve the instance or output that
# it is impossible
def getRes(d, p):
    # current score already ok
    if calc_score(p) <= d:
        return 0

    # need to change p with swaps       
    number_swaps = 0
    finished = False
    while not finished:
        p, finished = swap_next_s(p)
        number_swaps += 1
        if calc_score(p) <= d:
            return number_swaps

    # instance cannot be resolved with swaps
    return "IMPOSSIBLE"


# input and output
t = int(input())
for i in range(t):
    s = input().split()
    d = int(s[0])
    p = list(s[1])

    print("Case #" + str(i+1) + ": " + str(getRes(d, p)))
