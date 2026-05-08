# Problem: Product of Array Except Self
# Day: 8
# Approach: Division with zero handling

def itself(n):
    t = 1
    zero = 0
    f = []

    # total product of non-zero elements
    for i in range(len(n)):
        if n[i] == 0:
            zero += 1
        else:
            t *= n[i]

    # build answer
    for i in range(len(n)):

        # more than one zero
        if zero > 1:
            f.append(0)

        # exactly one zero
        elif zero == 1:
            if n[i] == 0:
                f.append(t)
            else:
                f.append(0)

        # no zero
        else:
            f.append(t // n[i])

    return f


n = list(map(int, input("enter numbers: ").split()))

print(itself(n))
