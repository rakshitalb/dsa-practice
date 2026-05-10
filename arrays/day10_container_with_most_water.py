# Problem: Container With Most Water
# Day: 10
# Approach: Two Pointers
# Time Complexity: O(n)

def water(height):

    l = 0
    r = len(height) - 1

    m = 0

    while l < r:

        area = min(height[l], height[r]) * (r - l)

        if area > m:
            m = area

        # move smaller height
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return m


height = list(map(int, input("enter heights: ").split()))

print(water(height))
