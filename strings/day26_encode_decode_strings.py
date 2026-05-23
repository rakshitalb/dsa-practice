# Problem: Encode and Decode Strings
# Day: 26
# Time Complexity: O(n)

def encode(words):

    s = ""

    for w in words:

        s += str(len(w)) + "#" + w

    return s


def decode(s):

    res = []

    i = 0

    while i < len(s):

        j = i

        # find #
        while s[j] != "#":
            j += 1

        # length of word
        l = int(s[i:j])

        # extract word
        word = s[j+1:j+1+l]

        res.append(word)

        # move pointer
        i = j + 1 + l

    return res


words = list(map(str, input("enter words: ").split()))

e = encode(words)

print("encoded:", e)

print("decoded:", decode(e))
