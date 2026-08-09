n = list(map(int,input("enter :").split()))
m = 0
c = 0

for i in range(len(n)):
    if n[i] == 1:
        c += 1
        m = max(m,c)
    else:
        c = 0

print(m)
