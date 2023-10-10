# Task 1: Function as a Parameter
# Write a Python function called apply_operation that takes three arguments:
# - operation: A function that takes two numeric arguments and performs a mathematical operation (e.g., add, subtract, multiply, divide).
# - operand1: The first numeric operand.
# - operand2: The second numeric operand.
# The apply_operation function should return the result of applying the operation function to operand1 and operand2. Test your function with at least two different operations.


def apply_operation(operation, operand1: int, operand2: int):
    return operation(operand1, operand2)


def add(x: int, y: int):
    return x + y


def subtract(x: int, y: int):
    return x - y

print(apply_operation(add, 5, 10))
print(apply_operation(subtract, 10, 5))
