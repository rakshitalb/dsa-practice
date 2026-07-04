# Problem: Jewels and Stones
# Day: 64

def jewels_stones(jewels, stones):

    count = 0

    for ch in stones:

        if ch in jewels:

            count += 1

    return count


jewels = input("enter jewels: ")

stones = input("enter stones: ")

print(jewels_stones(jewels, stones))
