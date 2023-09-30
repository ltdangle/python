# 3. Get a positive number from user input. Find all factors of this number.
#
#     Example:
#
#     - If the number is 6, the factors are: 1, 2, 3, 6
#
#     - If the number is 10, the factors are: 1, 2, 5, 10

while True:
    num = input("Input positive number: ")
    if num.isdigit() and int(num) > 0:
        num = int(num)
        break

i = 1
factors = []
while i <= num:
    if num % i == 0:
        factors.append(i)
    i=i+1 

print(factors)
