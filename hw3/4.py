# 4. Format string with proper built-in function.
# All letters must be written in lowercase.
string_1 = "Animals  "
print(string_1.lower())

# All letters must be capitalized.
string_2 = "  Badger"
print(string_2.upper())

# Remove all spaces:
string_3 = "   HoneyPot   "
# a) from the beginning of the line
print(string_3.lstrip())
# b) from the end of the line
print(string_3.rstrip())
# c) on both sides of the line
print(string_3.strip())

# Check the value of the startwith('Be') function for each line.:
string_1 = "Bear"
print(string_1.startswith("Be"))
string_2 = "bear"
print(string_2.startswith("Be"))
string_3 = "BEAR"
print(string_3.startswith("Be"))
string_4 = "bEar"
print(string_4.startswith("Be"))

# Convert these bear-like rows with methods from the previous exercise to have a positive result for each row.
print("\n")
formatted_string = string_2.capitalize()
print(formatted_string.startswith("Be"))

formatted_string = string_3.lower().capitalize()
print(formatted_string.startswith("Be"))

formatted_string = string_4.lower().capitalize()
print(formatted_string.startswith("Be"))
