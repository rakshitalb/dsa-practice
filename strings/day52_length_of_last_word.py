# Problem: Length of Last Word
# Day: 52

def last_word(s):

    words = s.split()

    return len(words[-1])


s = input("enter string: ")

print(last_word(s))
