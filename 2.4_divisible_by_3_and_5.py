'''
The problem
For a given number, find all the numbers smaller than the number. Numbers should be divisible by 3 and also by 5.

Hints
So, you have to check two conditions: make sure the number is divisible by 3, and also by 5. Hence, you will need to use two conditions.
'''

# Solution
print("Enter a number: ")
number = int(input())
for i in range(1, number):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
