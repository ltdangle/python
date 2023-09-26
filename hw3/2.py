# Get a string from user input. Check if the string is a palindrome.
s = input("Input a string: ")

palindrome = True

for index in range(len(s)):
    reverse_index = -index - 1

    if s[index] != s[reverse_index]:
        palindrome = False
        break

if palindrome:
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")
