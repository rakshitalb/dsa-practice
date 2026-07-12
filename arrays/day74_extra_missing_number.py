# Problem: Missing Number
# Day: 74 Extra

n = sorted(list(map(int, input("enter numbers: ").split())))

found = False

for i in range(1, len(n)):
    if n[i] - n[i - 1] != 1:
        print("missing number:", n[i - 1] + 1)
        found = True
        break

if found == False:
    print("missing number:", len(n))
