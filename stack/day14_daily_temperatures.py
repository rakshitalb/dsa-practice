# Problem: Daily Temperatures
# Day: 13
# Approach: Monotonic Stack
# Time Complexity: O(n)

def temp(t):

    res = [0] * len(t)

    stack = []

    for i in range(len(t)):

        while stack and t[i] > t[stack[-1]]:

            idx = stack.pop()

            res[idx] = i - idx

        stack.append(i)

    return res


t = list(map(int, input("enter temperatures: ").split()))

print(temp(t))
