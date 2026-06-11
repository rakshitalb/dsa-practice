seen = set()

n = int(input("enter number: "))

while True:

    if n in seen:
        print(False)
        break

    seen.add(n)

    digits = list(map(int, str(n)))

    result = 0

    for i in range(len(digits)):
        result += digits[i] ** 2

    if result == 1:
        print(True)
        break

    n = result
