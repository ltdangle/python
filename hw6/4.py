# 4. Write a function that implement case swapping. It should return the same result as swapcase() method. Your function should accept one str argument and convert all lower case values to upper case and vice versa.
#
# ```python
# def swapcase(input_string: str) -> str:
#     # do something
#
# print(swapcase('HelLo!'))
# >>> 'hELlO!
# ```


def swapcase(input_string: str) -> str:
    output = []
    for i in range(len(input_string)):
        if input_string[i].isupper():
            output.append(input_string[i].lower())
            continue
        output.append(input_string[i].upper())
    return "".join(output)


print(swapcase("HelLo!"))
