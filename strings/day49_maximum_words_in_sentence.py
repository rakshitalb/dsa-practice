# Problem: Maximum Number of Words Found in Sentences
# Day: 49

def max_words(sentences):

    maximum = 0

    for sentence in sentences:

        count = len(sentence.split())

        if count > maximum:

            maximum = count

    return maximum


n = int(input("enter number of sentences: "))

sentences = []

for i in range(n):

    sentences.append(input())

print(max_words(sentences))
