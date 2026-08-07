n = sorted(list(map(int, input("Enter : ").split())))

if n[0] != 0:
    print(0)

else:
    flag = False

    for i in range(1, len(n)):
        if n[i-1] != n[i] - 1:
            print(n[i] - 1)
            flag = True
            break

    if flag == False:
        print(n[-1] + 1)
