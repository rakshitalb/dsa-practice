# Problem: Two Sum
# Day: 76 Extra

n = list(map(int, input("enter numbers: ").split()))
t = int(input("enter target: "))

found = False

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] + n[j] == t:
            print(n[i], n[j])
            found = True
            break

    if found:
        break

if found == False:
    print("No pair found")
