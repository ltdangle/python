# Write a program that gets two int variables and swaps their values. Do it in 3 different ways.
a = 3
b = 5

# 1 
temp = a
a = b
b = temp

print("a =", a)
print("b =", b)

# 2 
a = 3
b = 5

a = a + b
b = a - b
a = a - b

print("a =", a)
print("b =", b)

# 3
a = 3
b = 5

a, b = b, a

print("a =", a)
print("b =", b)
