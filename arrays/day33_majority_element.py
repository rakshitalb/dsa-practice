# Problem: Majority Element
# Day: 33
# Time Complexity: O(n)

def majority(nums):

    d = {}

    for num in nums:

        if num in d:
            d[num] += 1

        else:
            d[num] = 1

    for key in d:

        if d[key] > len(nums) // 2:
            return key


nums = list(map(int, input("enter numbers: ").split()))

print(majority(nums))
