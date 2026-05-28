# Problem: Single Number
# Day: 31
# Time Complexity: O(n)

def single(nums):

    d = {}

    for num in nums:

        if num in d:
            d[num] += 1

        else:
            d[num] = 1

    for key in d:

        if d[key] == 1:
            return key


nums = list(map(int, input("enter numbers: ").split()))

print(single(nums))
