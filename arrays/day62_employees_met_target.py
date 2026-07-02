# Problem: Number of Employees Who Met the Target
# Day: 62

def employees(hours, target):

    count = 0

    for hour in hours:

        if hour >= target:

            count += 1

    return count


hours = list(map(int, input("enter hours: ").split()))

target = int(input("enter target: "))

print(employees(hours, target))
