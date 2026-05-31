# Problem: Intersection of Two Arrays
# Day: 34
# Time Complexity: O(n)

def inter(nums1, nums2):

    s = set(nums1)

    r = []

    for num in nums2:

        if num in s and num not in r:

            r.append(num)

    return r


nums1 = list(map(int, input("enter nums1: ").split()))

nums2 = list(map(int, input("enter nums2: ").split()))

print(inter(nums1, nums2))
