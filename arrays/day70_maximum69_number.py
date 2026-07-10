# Problem: Maximum 69 Number
# Day: 70

def maximum69(num):

    digits = list(str(num))

    for i in range(len(digits)):

        if digits[i] == "6":

            digits[i] = "9"

            break

    return int("".join(digits))


num = int(input("enter number: "))

print(maximum69(num))
