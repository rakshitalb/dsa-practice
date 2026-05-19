# Problem: Longest Consecutive Sequence
# Day: 22
# My Own Logic
# Time Complexity: O(n)

def long(n):

    s = set(n)

    m = []

    for i in s:

        if i + 1 in s or i - 1 in s:
            m.append(i)

    return len(m)


n = list(map(int, input("enter numbers: ").split()))

print(long(n))
