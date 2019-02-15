# codejam oversized pancake flipper
# https://code.google.com/codejam/contest/3264486/dashboard


def getRes(p, f):
	count = 0

	for ind, char in enumerate(p):
		# if we reach a "-" and can flip
		if char == "-": 
			if len(p) - ind >= f:
				p = flip(p, ind, f)
				count = count + 1
			else:
				return "IMPOSSIBLE"

	return str(count)


def flip(p, ind, f):
	newp = p
	# print(str(p) + " " + str(ind) + " " + str(f))
	for i in xrange(ind, ind + f):
		if p[i] == "-":
			newp[i] = "+"
		elif p[i] == "+":
			newp[i] = "-"
	return newp
   
    
# input and output
t = int(input())
for i in range(t):
    p, f = [s for s in raw_input().split()]
    print("Case #" + str(i+1) + ": " + getRes(list(p), int(f)))