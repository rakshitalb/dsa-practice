n = sorted(list(map(int, input("enter :").split())))
m = int(input("enter :"))
mm = float('inf')

for i in range(len(n)-m+1):
    diff = n[i+m-1] - n[i]
    mm = min(mm, diff)

print(mm)
