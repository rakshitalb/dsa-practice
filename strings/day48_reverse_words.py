# Problem: Reverse Words in a String III
# Day: 48
# Time Complexity: O(n)
# Space Complexity: O(n)

def reverse_words(s):

    words = s.split()

    result = []

    for word in words:
        result.append(word[::-1])

    return " ".join(result)


s = input("enter sentence: ")

print(reverse_words(s))
