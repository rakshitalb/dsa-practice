# Problem: Group Anagrams
# Day: 6
# Topic: Strings

def group_anagrams(arr):
    d = {}

    for word in arr:
        key = "".join(sorted(word))

        if key in d:
            d[key].append(word)
        else:
            d[key] = [word]

    return list(d.values())


arr = input("Enter words: ").split()

print(group_anagrams(arr))
