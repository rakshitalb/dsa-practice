# Problem: Count Asterisks
# Day: 55

def count_asterisks(s):

    inside = False

    count = 0

    for ch in s:

        if ch == "|":

            inside = not inside

        elif ch == "*" and inside == False:

            count += 1

    return count


s = input("enter string: ")

print(count_asterisks(s))
