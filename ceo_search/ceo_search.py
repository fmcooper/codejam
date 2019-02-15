# codejam ceo search
# https://codingcompetitions.withgoogle.com/codejamio/round/000000000005102c/0000000000050dd5


# Step up in experience level, keeping track of the number left to supervise. Subtract from this with each new experience level and then add to this with the number of new employees. At the end we need a ceo who has a larger experience level than anyone else AND who has to supervise all leftover people.
def getRes(a):
	numToSupervise = 0
	finale = 0
	for elem in a:
		n = elem[0]
		e = elem[1]
		finale = e

		numToSupervise = numToSupervise - (n * e)
		if numToSupervise < 0:
			numToSupervise = 0
		numToSupervise = numToSupervise + n

	return max(numToSupervise, e + 1)



# input and output
t = int(input())
for i in range(t):
    l = int(input())

    a = []
    for j in range(l):
        n,e = [int(s) for s in raw_input().split()]
        a.append((n, e))

    print("Case #" + str(i+1) + ": " + str(getRes(a)))