from colorama import Fore, init

#initialize colorama
init(autoreset=True)

# Basic Calculator Program

# Ask the user to input the first number
num1 = float(input("Enter the first number: "))

# Ask the user to input the second number
num2 = float(input("Enter the second number: "))

# Ask the user to input the mathematical operation (+, -, *, /)
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation and display the result
if operation == '+':
    result = num1 + num2
    print(Fore.GREEN + f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(Fore.GREEN + f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(Fore.GREEN + f"{num1} * {num2} = {result}")
elif operation == '/':
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
        print(Fore.GREEN + f"{num1} / {num2} = {result}")
    else:
        print(Fore.RED + "Error: Division by zero is not allowed.")
else:
    print(Fore.RED + "Invalid operation. Please enter +, -, *, or /.")
