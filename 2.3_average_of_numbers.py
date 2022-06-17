'''
The problem
Take numbers from a user and show the average of the numbers the user entered.

Hints
To solve this problem.
First, ask the user - How many numbers you want to enter?
Then, run a for-loop. Each time, take input from the user and put it in a list.
Once you get all the numbers, you can send the list to the sum function. The sum function will add all the numbers and give you the total.
Finally, divide the total by the number of elements the user entered.
That’s it.
'''

# Solution
print("How many numbers do you want to enter? ")
number_of_numbers = int(input())
numbers = []  # create an empty list
for i in range(number_of_numbers):
    print("Enter a number: ")
    numbers.append(int(input()))
print("The sum of the numbers is: ", sum(numbers))
print("The average of the numbers is: ", sum(numbers) / number_of_numbers)

# Alternate Solution
print("How many numbers do you want to enter? ")
number_of_numbers = int(input())
sum = 0
for i in range(number_of_numbers):
    print("Enter a number: ")
    sum += int(input())
print("The sum of the numbers is: ", sum)
print("The average of the numbers is: ", sum / number_of_numbers)
