# Problem: Group Anagrams
# Day: 23
# Time Complexity: O(n * k log k)

def ana(w):

    d = {}

    for s in w:

        k = "".join(sorted(s))

        if k in d:
            d[k].append(s)

        else:
            d[k] = [s]

    return list(d.values())


w = list(map(str, input("enter words: ").split()))

print(ana(w))
