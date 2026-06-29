# Problem: Truncate Sentence
# Day: 59

def truncate_sentence(s, k):

    words = s.split()

    return " ".join(words[:k])


s = input("enter sentence: ")

k = int(input("enter k: "))

print(truncate_sentence(s, k))
