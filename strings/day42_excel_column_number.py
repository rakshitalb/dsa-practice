# Problem: Excel Sheet Column Number
# Day: 42
# Time Complexity: O(n)

def column(title):

    result = 0

    for ch in title:

        value = ord(ch) - ord('A') + 1

        result = result * 26 + value

    return result


title = input("enter column title: ")

print(column(title))
