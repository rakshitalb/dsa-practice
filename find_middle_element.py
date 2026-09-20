n = list(map(int, input("enter : ").split()))

slow = 0
fast = 0

while fast < len(n) and fast + 1 < len(n):
    slow += 1
    fast += 2

print(n[slow])
