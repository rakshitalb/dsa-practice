n = list(map(int, input("enter : ").split()))

for i in range(len(n)):
    if n[i] in n[:i]:
        print(n[i])
        break
else:
    print(-1)
