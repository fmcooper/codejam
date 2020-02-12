# codejam cody's jams
# https://codingcompetitions.withgoogle.com/codejamio/round/0000000000051059/000000000005105a


# add to given dictionary (equals 1 for key that doesn't exist and 
# increments for key that does exist)
def add_to_d(d, k):
    if not k in d:
        d[k] = 1
    else:
        d[k] += 1


# decrementing the value of key in dictionary
def remove_from_d(d, k):
    num = d[k]
    d[k] -= 1


# iterates through the list of integers from highest to lowest. The
# highest remaining price must always be a full price.
def getRes(n):
    d = dict()
    for e in n:
        add_to_d(d, e)

    ans = ""
    for e in reversed(n):
        # find the next highest price
        if (d[e] > 0):
            sale = int(e * 3/4)
            ans = str(sale) + " " + ans
            # remove both full and sale price from our map
            remove_from_d(d, e)
            remove_from_d(d, sale)

    return ans


# input and output
t = int(input())
for i in range(t):
    input()
    n = [int(x) for x in input().split()]
    print("Case #" + str(i+1) + ": " + str(getRes(n)))
