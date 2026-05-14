# Problem: Binary Search
# Day: 15
# Time Complexity: O(log n)

def binary(nums, target):

    l = 0
    r = len(nums) - 1

    while l <= r:

        mid = (l + r) // 2

        # target found
        if nums[mid] == target:
            return mid

        # search right side
        elif nums[mid] < target:
            l = mid + 1

        # search left side
        else:
            r = mid - 1

    return -1


nums = list(map(int, input("enter sorted
