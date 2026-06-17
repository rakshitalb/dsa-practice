# Problem: Count Prefixes of a Given String
# Day: 48

def count_prefix(words, s):

    count = 0

    for word in words:

        if s.startswith(word):

            count += 1

    return count


words = input("enter words: ").split()

s = input("enter string: ")

print(count_prefix(words, s))
