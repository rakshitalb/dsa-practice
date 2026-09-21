nums = list(map(int, input("Enter array: ").split()))

slow = 0

for fast in range(len(nums)):
    if nums[fast] != 0:
        nums[slow], nums[fast] = nums[fast], nums[slow]
        slow += 1

print("Array after moving zeroes:", nums)
