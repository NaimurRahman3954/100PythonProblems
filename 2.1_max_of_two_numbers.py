'''
The problem
Find the max number of two numbers.

Hints
Ask the user to enter two numbers.

Then, you can run a comparison to compare which one is larger.

Think about it and try yourself first.
'''

# Solution
print("Enter a number: ")
number1 = int(input())
print("Enter another number: ")
number2 = int(input())
if number1 > number2:

    print(number1, "is larger than", number2)
else:
    print(number2, "is larger than", number1)
