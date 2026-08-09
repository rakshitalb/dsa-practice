n = sorted(list(map(int,input("enter :").split())))
m = 1
c = 1

for i in range(1,len(n)):
    if n[i] == n[i-1]:
        continue
    elif n[i-1] == n[i]-1:
        c += 1
    else:
        c = 1
    m = max(c,m)

m = max(c,m)
print(m)
