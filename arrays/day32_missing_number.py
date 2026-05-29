# Problem: Missing Number
# Day: 32
# Time Complexity: O(n)

def missing(nums):

    n = len(nums)

    expected = n * (n + 1) // 2

    actual = sum(nums)

    return expected - actual


nums = list(map(int, input("enter numbers: ").split()))

print(missing(nums))
