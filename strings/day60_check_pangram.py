# Problem: Check if the Sentence Is Pangram
# Day: 60

def pangram(sentence):

    return len(set(sentence)) == 26


sentence = input("enter sentence: ")

print(pangram(sentence))
