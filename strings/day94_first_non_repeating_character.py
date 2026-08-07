n = input("enter : ")
d = {}

for ch in n:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] += 1

flag = False

for ch in n:
    if d[ch] == 1:
        print(ch)
        flag = True
        break

if flag == False:
    print(-1)
