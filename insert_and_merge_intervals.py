ii = list(map(int, input("enter :").split()))
ni = list(map(int, input("enter :").split()))

a = []
ai = []

for i in range(0, len(ii), 2):
    a.append([ii[i], ii[i+1]])

for i in range(0, len(ni), 2):
    ai.append([ni[i], ni[i+1]])

a = a + ai
a.sort()

ans = []

for i in a:
    if not ans or ans[-1][1] < i[0]:
        ans.append(i)
    else:
        ans[-1][1] = max(ans[-1][1], i[1])

print(ans)
