n = list(map(int, input("Enter: ").split()))

if len(n) == 1:
    print(0)

elif n[0] > n[1]:
    print(0)

elif n[-1] > n[-2]:
    print(len(n) - 1)

else:
    for i in range(1, len(n) - 1):
        if n[i] > n[i - 1] and n[i] > n[i + 1]:
            print(i)
            break
