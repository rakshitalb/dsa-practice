# Problem: Majority Element
# Day: 74

n = list(map(int, input("enter numbers: ").split()))

count = 1
maj = {n[0]: count}

for i in range(1, len(n)):
    if n[i] in maj:
        maj[n[i]] += 1
    else:
        maj[n[i]] = count

found = False

for key, value in maj.items():
    if value > len(n) // 2:
        print(key)
        found = True
        break

if found == False:
    print("No majority element")
