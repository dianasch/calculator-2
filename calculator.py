

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )




def prefix_notation_calculator():
    """CLI application for a prefix-notation calculator."""
    try:
    

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
        elif operation_input[0] == "pow":
            return power(operation_input[1], operation_input[2])
        elif operation_input[0] == "mod":
            return mod(operation_input[1], operation_input[2])
    except IndexError:
        operation_input[1] = float(operation_input[1])
        if operation_input[0] == "square":
            return square(operation_input[1])
        elif operation_input[0] == "cube":
            return cube(operation_input[1])
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
