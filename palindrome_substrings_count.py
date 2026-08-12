n = list(map(str, input("enter :")))
ans = []

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if i != j:
            window = n[i:j + 1]

            if window == window[::-1]:
                ans.append("".join(window))

print(ans)
print(len(ans))
