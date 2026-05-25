# Problem: Move Zeroes
# Day: 28
# Time Complexity: O(n)

def zero(nums):

    l = 0

    for r in range(len(nums)):

        if nums[r] != 0:

            nums[l], nums[r] = nums[r], nums[l]

            l += 1

    return nums


nums = list(map(int, input("enter numbers: ").split()))

print(zero(nums))
