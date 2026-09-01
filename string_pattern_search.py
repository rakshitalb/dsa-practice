# Find the first occurrence of a word in a string

h = input("haystack: ")
n = input("needle: ")

i = 0

while i < len(h):
    j = 0

    while j < len(n) and i + j < len(h) and h[i + j] == n[j]:
        j += 1

    if j == len(n):
        print(i)
        break

    i += 1

else:
    print(-1)
