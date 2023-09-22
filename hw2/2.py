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

first_num = int(first_num)
second_num = int(second_num)

difference = first_num - second_num

print(f"The difference is: {difference}")
