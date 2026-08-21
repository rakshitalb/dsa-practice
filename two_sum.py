# Find two elements whose sum equals the target

n = list(map(int, input("enter : ").split()))
target = int(input("target : "))

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] + n[j] == target:
            print([i, j])
            break
