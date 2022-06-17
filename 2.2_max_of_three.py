'''
The problem
Find the largest of the three numbers.

Hints
Ask the user to enter three numbers.

Then, you can run multiple comparisons to compare which one is the largest.

At first, you can consider that the first number is the largest.

Then compare the second number with the first number and the third number. If the second number is greater or equal to the first number and the second number is greater or equal to the third number, then the second number is the largest.

Similarly, compare the third number with the first or second number.

Otherwise, the first number will be the largest.

Think about it. And try yourself first.
'''

# Solution
print("Enter a number: ")
number1 = int(input())
print("Enter another number: ")
number2 = int(input())
print("Enter another number: ")
number3 = int(input())
if number1 > number2 and number1 > number3:
    print(number1, "is the largest")
elif number2 > number1 and number2 > number3:
    print(number2, "is the largest")
else:
    print(number3, "is the largest")

# Alternate Solution
print("Enter a number: ")
number1 = int(input())
print("Enter another number: ")
number2 = int(input())
print("Enter another number: ")
number3 = int(input())
# max function is used to find the max number of three numbers
print(max(number1, number2, number3), "is the largest")
