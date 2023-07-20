import math

def calc():
    equation = input("Enter your math problem: ")
    problem = equation.split(" ")
    num1 = int(problem[0])
    num2 = int(problem[2])
    operator = problem[1]

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operation"

print(calc())

