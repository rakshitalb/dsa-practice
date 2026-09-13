n = list(input("enter :"))

ans = []

for ch in n:
    if ans and ans[-1] == ch:
        ans.pop()
    else:
        ans.append(ch)

print("".join(ans))
