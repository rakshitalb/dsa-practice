# Problem: Contains Duplicate
# Day: 37
# Time Complexity: O(n)

def duplicate(nums):

    s = set()

    for num in nums:

        if num in s:
            return True

        s.add(num)

    return False


nums = list(map(int, input("enter numbers: ").split()))

print(duplicate(nums))
