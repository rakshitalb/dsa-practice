# Find leaders in an array

arr = list(map(int, input("enter :").split()))
l = 0
le = []

while l < len(arr):
    if all(arr[l] > x for x in arr[l+1:]):
        le.append(arr[l])
    l += 1

print(le)
