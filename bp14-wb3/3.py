# Task 3: Function as an Element of a List
#
# Create a list called operation_list that contains three functions: add, subtract, and multiply. Each of these functions should take two numeric arguments and perform the respective operation. For example, add(3, 5) should return 8.
#
# Iterate through the operation_list and apply each operation to a pair of numbers. Print the results.


def add(a: int, b: int):
    return a + b


def subtract(a: int, b: int):
    return a - b


def multiply(a: int, b: int):
    return a * b


operation_list = [add, subtract, multiply]

for operation in operation_list:
    print(operation(3, 5))
