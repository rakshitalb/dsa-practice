# Problem: Valid Parentheses
# Day: 72

def valid_parentheses(brackets):

    push = []

    d = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for ch in brackets:

        if ch == "(" or ch == "[" or ch == "{":

            push.append(ch)

        elif ch == ")" or ch == "]" or ch == "}":

            if len(push) == 0:
                return False

            if push.pop() != d[ch]:
                return False

    return len(push) == 0


brackets = input("enter brackets: ")

print(valid_parentheses(brackets))
