str1 = input("Enter strings: ")
d = str1.split()

prefix = d[0]

for i in range(1, len(d)):
    while d[i].find(prefix) != 0:
        prefix = prefix[:-1]
        if prefix == "":
            break

print(prefix)
