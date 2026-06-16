# Problem: Find Words Containing Character
# Day: 47

def find_words(words, x):

    result = []

    for i in range(len(words)):

        if x in words[i]:
            result.append(i)

    return result


words = input("enter words: ").split()

x = input("enter character: ")

print(find_words(words, x))
