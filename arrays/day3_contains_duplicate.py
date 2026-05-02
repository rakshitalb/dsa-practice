# Problem: Contains Duplicate
# Day: 3

def containsDuplicate(nums):
    return len(nums) != len(set(nums))
nums = list(map(int, input("Enter numbers (space separated): ").split()))

result = containsDuplicate(nums)

print("Contains Duplicate:", result)
