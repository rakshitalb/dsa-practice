h = input("haystack: ")
n = input("needle: ")

g = "".join(n)
r = "".join(h)

if g in r:
    for i in range(len(h) - len(n) + 1):
        if h[i:i + len(n)] == n:
            print(i)
            break
else:
    print(-1)
