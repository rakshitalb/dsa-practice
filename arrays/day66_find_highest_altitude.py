# Problem: Find the Highest Altitude
# Day: 66

def highest_altitude(gain):

    altitude = 0

    highest = 0

    for value in gain:

        altitude += value

        if altitude > highest:

            highest = altitude

    return highest


gain = list(map(int, input("enter gain: ").split()))

print(highest_altitude(gain))
