# Problem: Contains Duplicate
# Day: 17
# Without using set
# Time Complexity: O(n)

def duplicate(nums):

    d = {}

    for num in nums:

        if num in d:
            return True

        d[num] = 1

    return False


nums = list(map(int, input("enter numbers: ").split()))

print(duplicate(nums))
