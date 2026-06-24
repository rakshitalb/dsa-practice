# Problem: Maximum Number of String Pairs
# Day: 54

def string_pairs(words):

    count = 0

    for i in range(len(words)):

        for j in range(i + 1, len(words)):

            if words[i] == words[j][::-1]:

                count += 1

    return count


words = input("enter words: ").split()

print(string_pairs(words))
