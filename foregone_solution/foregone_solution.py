# codejam foregone solution
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231


# look at each digit in turn. If the number is 4 then add two
# to each of a and b. Otherwise add digit to a and 0 to b. 
def getRes(q):
	a, b = "", ""
	for c in q:
		digit = int(c)
		if digit == 4:
			a += "2"
			b += "2"
		else:
			a += str(digit)
			b += "0"
	return a, b


# input and output
t = int(input())
for i in range(t):
    q = input()
    print("Case #" + str(i+1) + ": " + str(getRes(q)[0]) \
    + " " + str(getRes(q)[1]))
