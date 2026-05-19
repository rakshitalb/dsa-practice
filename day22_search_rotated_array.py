# Problem: Search in Rotated Sorted Array
# Approach: Linear Search
# Time Complexity: O(n)
def ind(t,n):
    for i in range(len(n)):
        if n[i] == t:
            return i
    else:
        return -1
n = list(map(int, input("enter list of numbers: ").split()))
t = int(input("enter t:"))
print(ind(t,n))
