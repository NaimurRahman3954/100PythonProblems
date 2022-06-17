'''
The problem
Swap two variables.

To swap two variables: the value of the first variable will become the value of the second variable. On the other hand, the value of the second variable will become the value of the first variable.

Hints
To swap two variables, you can use a temp variable.
'''
# Solution
a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)

# Alternate Solution
a = 10
b = 20
a = a+b
b = a-b
a = a-b
print(a, b)

# Alternate Solution
a = 10
b = 20
a, b = b, a  # using comma operator to swap the values of a and b
print(a, b)
