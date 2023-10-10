# 1. Write a program that asks user to enter an integer and convert it to int. The program should have 2 functions. The first function should ask user to input an information and return inputted value. The second function that receives the inputted value and converts it to int. If the user enters something that is not an integer, this function should catch an error and ask the user to enter an integer again. if user inputs an integer, program should print this number and quit w/o any error.


def loop():
    while True:
        try:
            val = int(get_user_input())
        except Exception:
            print("Wrong input, please enter integers.")
            continue
        break
    print(f"You entered: {val}")


def get_user_input() -> str:
    return input("Enter integers: ")


loop()
