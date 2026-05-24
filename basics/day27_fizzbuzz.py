# Problem: Fizz Buzz
# Day: 27
# Time Complexity: O(n)

def fizzbuzz(n):

    for i in range(1, n + 1):

        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")

        elif i % 3 == 0:
            print("Fizz", end=" ")

        elif i % 5 == 0:
            print("Buzz", end=" ")

        else:
            print(i, end=" ")


n = int(input("enter number: "))

fizzbuzz(n)
