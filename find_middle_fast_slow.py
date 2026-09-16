n = list(map(int, input("enter :").split()))

slow = 0
fast = 0

while fast < len(n) - 1:
    slow += 1
    fast += 2

print(n[slow])
