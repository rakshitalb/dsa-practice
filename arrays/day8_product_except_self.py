# Problem: Product of Array Except Self
# Day: 8
# Time Complexity: O(n)

def product(nums):
    n = len(nums)

    left = [1] * n
    right = [1] * n
    ans = [1] * n

    # left product
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]

    # right product
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]

    # final answer
    for i in range(n):
        ans[i] = left[i] * right[i]

    return ans


nums = list(map(int, input("enter numbers: ").split()))

print(product(nums))
