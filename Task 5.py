# Function to perform addition
def ADD(a, b):
    return a + b

# Function to perform subtraction
def SUB(a, b):
    return a - b

# Function to calculate the square of a number
def SQUARE(a):
    return a ** 2

# Function to calculate the cube of a number
def CUBE(a):
    return a ** 3

# Take user input for the first number
a = int(input("Enter 1st Number: "))

# Take user input for the operator
b = input("Enter The Operator: ")

# Check the operator and perform the corresponding operation
if b == "+":
    # If the operator is '+', take input for the second number and perform addition
    b = int(input("Enter the 2nd Number: "))
    result = ADD(a, b)
    print("Your Result is: %d" % result)
elif b == "-":
    # If the operator is '-', take input for the second number and perform subtraction
    b = int(input("Enter the 2nd Number: "))
    result = SUB(a, b)
    print("Your Result is: %d" % result)
elif b == "s":
    # If the operator is 's', calculate the square of the number
    result = SQUARE(a)
    print("Your Result is: %d" % result)
elif b == "c":
    # If the operator is 'c', calculate the cube of the number
    result = CUBE(a)
    print("Your Result is: %d" % result)
else:
    # If an invalid operator is entered, display an error message
    print("Invalid operator. Please enter +, -, s, or c.")
