n = eval(input("Enter intervals: "))

n.sort()

ans = []

for interval in n:

    if not ans or ans[-1][1] < interval[0]:
        ans.append(interval)

    else:
        ans[-1][1] = max(ans[-1][1], interval[1])

print(ans)
