def exself(n):

    f = []

    for i in range(len(n)):

        p = 1

        for j in range(len(n)):

            if i != j:

                p *= n[j]

        f.append(p)

    return f


n = list(map(int, input("enter numbers: ").split()))

print(exself(n))
