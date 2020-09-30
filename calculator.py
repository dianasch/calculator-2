"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )




def prefix_notation_calculator():
    """Take in an operation and 2 numbers and perform the operation """

    operation_input[1] = float(operation_input[1])
    operation_input[2] = float(operation_input[2])
    if operation_input[0] == "+":
        return add(operation_input[1], operation_input[2])
    elif operation_input[0] == "-":
        return subtract(operation_input[1], operation_input[2])
    elif operation_input[0] == "*":
        return multiply(operation_input[1], operation_input[2])
    elif operation_input[0] == "/":
        return divide(operation_input[1], operation_input[2])
    elif operation_input[0] == "square":
        return square(operation_input[1], operation_input[2])
    elif operation_input[0] == "cube":
        return cube(operation_input[1], operation_input[2])
    elif operation_input[0] == "pow":
        return power(operation_input[1], operation_input[2])

while True:
    user_calculation = input()
    # read input
    # tokenize input
    operation_input = user_calculation.split()
   
    #     if the first token is "q":

    if operation_input[0] == "q":
        break  
    else:
        print(prefix_notation_calculator())
# Replace this with your code
