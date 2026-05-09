# Problem: 3Sum
# Day: 9
# Approach: Sorting + Two Pointers
# Time Complexity: O(n^2)

def tsum(n, tr):
    n.sort()
    f = []
    for i in range(len(n) - 2):
        l = i + 1
        r = len(n) - 1
        while l < r:
            s = n[i] + n[l] + n[r]
            if s == tr:
                f.append([n[i], n[l], n[r]])
                l += 1
                r -= 1
            elif s < tr:
                l += 1
            else:
                r -= 1
    return f
n = list(map(int, input("enter list: ").split()))
tr = int(input("enter target: "))
print(tsum(n, tr))
