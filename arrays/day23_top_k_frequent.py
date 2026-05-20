# Problem: Top K Frequent Elements
# Day: 23
# My Own Logic
# Time Complexity: O(n)

def freq(n,k):

    d = {}

    for num in n:

        if num in d:
            d[num] += 1

        else:
            d[num] = 1

    if max(d.values()) > k:
        del d[num]

    return list(d.keys())


n = list(map(int, input("enter numbers: ").split()))

k = int(input("enter k :"))

print(freq(n,k))
