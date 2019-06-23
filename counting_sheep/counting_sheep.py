# codejam cruise control
# https://code.google.com/codejam/contest/6254486/dashboard


def findFinalNum(a):
    if a == 0:
        return "INSOMNIA"

    seen = [False] * 10
    seen_count = 0
    recent_num = a
    
    # keep going until seen all digits
    mult = 1
    while True:

        # save the digits I have seen
        str_digits = str(recent_num)
        for char in str_digits:
            if seen[int(char)] == False:
                seen[int(char)] = True
                seen_count = seen_count + 1
                # if we have seen all digits return the most recent number
                if seen_count == 10:
                    return recent_num

        mult = mult + 1
        recent_num = a * mult


# input and output
n = int(input())
for i in range(n):
    a = int(raw_input())

    print("Case #" + str(i+1) + ": " + str(findFinalNum(a)))

