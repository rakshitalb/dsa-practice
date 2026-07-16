arr1 = list(map(int, input("enter: ").split()))
arr2 = list(map(int, input("enter: ").split()))

arr = []

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            arr.append(arr1[i])

print(set(arr))
