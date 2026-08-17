# Find the duplicate number in an array

n = list(map(int, input("enter :").split()))

s = []

for i in range(len(n)):
    if n[i] in s:
        print(n[i])
        break
    else:
        s.append(n[i])
