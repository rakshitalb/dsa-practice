n = int(input("Enter number of intervals: "))

intervals = []

for i in range(n):
    s, e = map(int, input().split())
    intervals.append([s, e])

intervals.sort()

ans = [intervals[0]]

for i in range(1, len(intervals)):
    if ans[-1][1] >= intervals[i][0]:
        ans[-1][1] = max(ans[-1][1], intervals[i][1])
    else:
        ans.append(intervals[i])

print(ans)
