n = sorted(list(map(int,input("enter :").split())))
ans = 0
sec = 0
tr = 0

if len(n) < 3:
    print(-1)
else:
    for i in range(len(n)):
        if n[i] >= ans:
            tr = sec
            sec = ans
            ans = n[i]

    print(tr)
