# Task 2: Function as a Return Value
#
# Create a function called get_multiplier that takes a single numeric argument multiplier. Inside this function, define and return another function (inner function) that takes a single numeric argument number and returns the result of multiplying number by multiplier.
#
# Write a code snippet to demonstrate the use of get_multiplier. Use the returned function to multiply a number by different multipliers.


def get_multiplier(multiplier: int):
    def inner_function(number: int):
        return number * multiplier

    return inner_function


double = get_multiplier(2)
triple = get_multiplier(3)

print(double(4))
print(triple(4))
