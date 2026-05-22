# Problem: Top K Frequent Elements
# Day: 25
# Time Complexity: O(n log n)

def topk(nums, k):

    d = {}

    # count frequency
    for num in nums:

        if num in d:
            d[num] += 1

        else:
            d[num] = 1

    # sort by frequency
    s = sorted(d, key=d.get, reverse=True)

    return s[:k]


nums = list(map(int, input("enter numbers: ").split()))

k = int(input("enter k: "))

print(topk(nums, k))
