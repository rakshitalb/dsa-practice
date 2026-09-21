nums = list(map(int, input("Enter sorted array: ").split()))

if len(nums) == 0:
    print("Array is empty")
else:
    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    print("Unique elements:", nums[:slow + 1])
    print("Number of unique elements:", slow + 1)
