# Problem: Remove Duplicates from Sorted Array
# Day: 53

def remove_duplicates(nums):

    return len(set(nums))


nums = list(map(int, input("enter numbers: ").split()))

print(remove_duplicates(nums))
