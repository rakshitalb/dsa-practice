nums1 = list(map(int, input("Enter first array: ").split()))
nums2 = list(map(int, input("Enter second array: ").split()))

nums1.sort()
nums2.sort()

i = 0
j = 0

ans = []

while i < len(nums1) and j < len(nums2):

    if nums1[i] == nums2[j]:
        ans.append(nums1[i])
        i += 1
        j += 1

    elif nums1[i] < nums2[j]:
        i += 1

    else:
        j += 1

print("Intersection:", ans)
