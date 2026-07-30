n = list(map(int, input("Enter: ").split()))

s = set(n)
longest = 0

for num in s:

    # Start of a sequence
    if num - 1 not in s:

        current = num
        length = 1

        while current + 1 in s:
            current += 1
            length += 1

        longest = max(longest, length)

print(longest)
