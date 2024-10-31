# Cole Jordan
# UWYO COSC 1010
# 10/31/24
# Lab 7
# Lab Section: 12 
# Sources, people worked with, help given to: Peter Martinez


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

factorialBound = str(input("Enter Upper Bound: !"))
factorial = 1

while not factorialBound.isdigit():
    factorialBound = str(input("Input Error, Enter a Real Number: !"))

for i in range(1,int(factorialBound) + 1):
    factorial = factorial * i

print(f"The result of the factorial based on the given bound is {factorial}")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

def isNegative(input):
    if input.startswith('-'):
        return True
    else:
        return False

def isNum(input):
    if input.isdigit():
        return True
    else:
        return False

def numChecker(input):
    number = input
    if isNegative(input):
        number = number.replace('-','')
        return isNum(number)    
    else:
        return isNum(number)


    
sum = 0

while True:
    currentNumber = str(input(f"Current Sum: {sum}, Input Number Here, Type 'exit' to Exit: "))

    # Exit Checker

    if currentNumber.lower() == 'exit':
        break

    # Checks if number, loops prompting for a proper input if not, while accounting for negative

    elif not numChecker(currentNumber):
        print('Not a number, try again!')
        continue

    

    if currentNumber.startswith('-'):
        sum = sum - int(currentNumber.replace('-', ''))
    else:
        sum += int(currentNumber)
    
    






print(f"Your final sum is {sum}")

print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input

def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def divide(num1, num2):
    return num1/num2

def multiply(num1,num2):
    return num1*num2

def remainder(num1,num2):
    return num1%num2

while True:
    calculatorInput = str(input("Type 'exit' to Exit. Enter Full Calculator Operation Here: "))

    if calculatorInput.lower() == 'exit':
        break

    operator = ''
    statusChecker = False

    for i in calculatorInput:
        if not i.isdigit():
            if i == '+' or i == '-' or i =='*' or i == '/' or i == '%':
                operator = i
            else:
                print("Not a Proper Input, Try Again")
                statusChecker = True

    if statusChecker:
        continue

    numList = calculatorInput.split(operator)

    numList[0] = int(numList[0])
    numList[1] = int(numList[1])

    result = 0

    if operator == '+':
        result = add(numList[0],numList[1])
    elif operator == '-':
        result = subtract(numList[0],numList[1])
    elif operator == '*':
        result = multiply(numList[0],numList[1])
    elif operator == '/':
        result = divide(numList[0],numList[1])
    elif operator == '%':
        result = remainder(numList[0],numList[1])

    print(f"The Result of your Calculator Operation is {result}")
