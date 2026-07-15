# Problem: Find the Duplicate Number
# Day: 77

n = list(map(int, input("enter numbers: ").split()))

seen = set()
found = False

for num in n:
    if num in seen:
        print("Duplicate:", num)
        found = True
        break
    else:
        seen.add(num)

if found == False:
    print("No duplicate")
