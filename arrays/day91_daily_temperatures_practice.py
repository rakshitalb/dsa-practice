n = list(map(int, input("Enter: ").split()))

for i in range(len(n)):
    found = 0

    for j in range(i + 1, len(n)):
        if n[j] > n[i]:
            print(j - i)
            found = 1
            break

    if found == 0:
        print(0)
