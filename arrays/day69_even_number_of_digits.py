# Problem: Find Numbers with Even Number of Digits
# Day: 69

def even_digits(nums):

    count = 0

    for num in nums:

        if len(str(num)) % 2 == 0:

            count += 1

    return count


nums = list(map(int, input("enter numbers: ").split()))

print(even_digits(nums))
