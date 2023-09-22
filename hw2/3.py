while True:
     try:
      first_num = int(input("Enter the first digit: "))
      break
     except ValueError:
       print("Oops! That was not a valid number. Try again...")
 
while True:
     try:
      second_num = int(input("Enter the second digit: "))
      break
     except ValueError:
       print("Oops! That was not a valid number. Try again...")

maximum_value = max(first_num, second_num)
print(f"The maximum is: {maximum_value}")
