# Problem: Sort Array by Parity
# Day: 61

def sort_parity(nums):

    even = []
    odd = []

    for num in nums:

        if num % 2 == 0:

            even.append(num)

        else:

            odd.append(num)

    return even + odd


nums = list(map(int, input("enter numbers: ").split()))

print(sort_parity(nums))
