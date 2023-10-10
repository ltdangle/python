# Task 4: Function as a Dictionary Value
#
# Create a dictionary called operation_dict with keys add, subtract, and multiply. The values for each key should be the corresponding operation function (e.g., the 'add' key should map to the add function).
#
# Prompt the user to enter a key from the dictionary (add, subtract, or multiply) and two numeric values. Use the selected function from operation_dict to perform the operation on the numeric values and display the result.


def add(a:int, b:int):
    return a + b


def subtract(a:int, b:int):
    return a - b


def multiply(a:int, b:int):
    return a * b


operation_dict = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply
}

key = input('Please enter an operation (add, subtract, or multiply): ')
num1 = int(input('Please enter the first number: '))
num2 = int(input('Please enter the second number: '))

result = operation_dict[key](num1, num2)
print(f'The result is {result}')
