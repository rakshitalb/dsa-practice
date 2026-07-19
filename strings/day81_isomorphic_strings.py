str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) != len(str2):
    print(False)
    exit()

d1 = {}
d2 = {}

for i in range(len(str1)):
    if str1[i] not in d1 and str2[i] not in d2:
        d1[str1[i]] = str2[i]
        d2[str2[i]] = str1[i]

    elif d1.get(str1[i]) != str2[i] or d2.get(str2[i]) != str1[i]:
        print(False)
        exit()

print(True)
