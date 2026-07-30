n = list(map(int, input("Enter: ").split()))

red = []
white = []
blue = []

for num in n:
    if num == 0:
        red.append(num)
    elif num == 1:
        white.append(num)
    elif num == 2:
        blue.append(num)

print(red + white + blue)
