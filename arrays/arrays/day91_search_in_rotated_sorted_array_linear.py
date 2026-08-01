n = list(map(int, input("Enter: ").split()))
t = int(input("Enter t: "))

for i in range(len(n)):
    if n[i] == t:
        print(i)
        break

if t not in n:
    print(-1)
