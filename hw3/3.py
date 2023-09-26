# The program receives the user's name and age from the input.
name = input("Your name: ")

while True:
    try:
        age = input("Your age: ")
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")
# Then you need to display the name and age in one line in several ways:

# - by listing all the parameters in the print function
print("Your name is " + name + " and your age is " + age + " years old.")

# - by formatting a string using the format function
print(
    "Your name is {name}  and your age is {age} years old.".format(name=name, age=age)
)

# - by formatting a string with f-string
print(f"Your name is {name} and your age is {age}  years old.")


