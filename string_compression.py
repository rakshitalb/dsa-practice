n = list(input("Enter characters: ").split())

write = 0
read = 0

while read < len(n):
    char = n[read]
    count = 0

    while read < len(n) and n[read] == char:
        count += 1
        read += 1

    n[write] = char
    write += 1

    if count > 1:
        for digit in str(count):
            n[write] = digit
            write += 1

print(n[:write])
