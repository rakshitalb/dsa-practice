n = list(map(int, input("Enter: ").split()))

s = set(n)

if len(s) != len(n):
    print(True)
else:
    print(False)
