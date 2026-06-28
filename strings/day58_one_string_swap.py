# Problem: Check if One String Swap Can Make Strings Equal
# Day: 58

def one_swap(s1, s2):

    if s1 == s2:
        return True

    diff = []

    for i in range(len(s1)):

        if s1[i] != s2[i]:

            diff.append(i)

    if len(diff) != 2:
        return False

    i, j = diff

    return s1[i] == s2[j] and s1[j] == s2[i]


s1 = input("enter first string: ")
s2 = input("enter second string: ")

print(one_swap(s1, s2))
