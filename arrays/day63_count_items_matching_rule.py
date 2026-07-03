# Problem: Count Items Matching a Rule
# Day: 63

def count_matches(items, ruleKey, ruleValue):

    if ruleKey == "type":
        index = 0

    elif ruleKey == "color":
        index = 1

    else:
        index = 2

    count = 0

    for item in items:

        if item[index] == ruleValue:

            count += 1

    return count


n = int(input("enter number of items: "))

items = []

for i in range(n):

    items.append(input().split())

ruleKey = input("enter ruleKey (type/color/name): ")

ruleValue = input("enter ruleValue: ")

print(count_matches(items, ruleKey, ruleValue))
