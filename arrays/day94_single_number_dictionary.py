n = list(map(int, input("Enter : ").split()))
ans = {}

for num in n:
    if num not in ans:
        ans[num] = 1
    else:
        ans[num] += 1

for key, value in ans.items():
    if value == 1:
        print(key)
