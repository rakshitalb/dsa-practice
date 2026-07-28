n = list(map(int, input("Enter: ").split()))
t = int(input("Enter t: "))

s = -1

for i in range(len(n)):
    if n[i] == t:
        s = i
        break

print(s)
