# 2. Write a program that asks user to input a string and an integer `n`. The Program should have 2 functions. The first function should ask user to enter string and integer. The second function should receive the inputted value and print the character at index `n`. If the user enters wrong value, this function should catch an error and provide a proper error message with an explanation. After the error is handled, the program should ask the user to enter a string and an integer again. If user inputs a string and an integer, program should print the character at index `n` and quit w/o any error.
def ask_for_input():
    str_input = input("Please enter a string: ")
    int_input = input("Please enter an integer: ")
    return str_input, int_input


def print_character_at_index():
    while True:
        try:
            user_string, user_integer = ask_for_input()
            user_integer = int(user_integer)
            print(
                f"The character at index {user_integer} is: {user_string[user_integer]}"
            )
            break
        except ValueError:
            print("You didn't enter a valid integer. Try again.")
        except IndexError:
            print("Your integer was out of the range of the string. Try again.")

print_character_at_index()
