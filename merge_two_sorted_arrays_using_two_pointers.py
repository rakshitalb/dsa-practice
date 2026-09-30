nums1 = list(map(int, input("Enter first sorted array: ").split()))
nums2 = list(map(int, input("Enter second sorted array: ").split()))

i = 0
j = 0

ans = []

while i < len(nums1) and j < len(nums2):

    if nums1[i] < nums2[j]:
        ans.append(nums1[i])
        i += 1
    else:
        ans.append(nums2[j])
        j += 1

while i < len(nums1):
    ans.append(nums1[i])
    i += 1

while j < len(nums2):
    ans.append(nums2[j])
    j += 1

print("Merged array:", ans)
