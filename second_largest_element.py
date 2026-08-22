n = list(map(int, input("enter : ").split()))

large = float('-inf')
second = float('-inf')

for i in range(len(n)):
    if n[i] > large:
        second = large
        large = n[i]
    elif n[i] > second and n[i] != large:
        second = n[i]

print(second)
