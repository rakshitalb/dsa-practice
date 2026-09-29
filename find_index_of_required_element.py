nums = list(map(int, input("Enter numbers: ").split()))

target = int(input("Enter required number: "))

index = -1

for i in range(len(nums)):
    if nums[i] == target:
        index = i
        break

if index != -1:
    print("Index:", index)
else:
    print("Number not found")
