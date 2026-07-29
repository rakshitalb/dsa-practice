n = list(map(int, input("Enter: ").split()))
t = int(input("Enter target: "))

d = {}

for i in range(len(n)):
    diff = t - n[i]

    if diff in d:
        print(diff, n[i])
        print(d[diff], i)
        break

    d[n[i]] = i
