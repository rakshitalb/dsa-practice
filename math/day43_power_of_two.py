# Problem: Power of Two
# Day: 43
# Time Complexity: O(log n)

def power(n):

    if n <= 0:
        return False

    while n % 2 == 0:

        n = n // 2

    return n == 1


n = int(input("enter number: "))

print(power(n))
