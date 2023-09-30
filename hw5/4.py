# 4. Write a Python program to check whether a triangle is equilateral, isosceles or scalene. Get all three sides from user input.
#
#     Note :
#
# An equilateral triangle is a triangle in which all three sides are equal.A scalene triangle is a triangle that has three unequal sides.An isosceles triangle is a triangle with (at least) two equal sides.
while True:
    side1 = input("Input first side: ")
    if side1.isdigit() and int(side1) > 0:
        side1 = int(side1)
        break
while True:
    side2 = input("Input second side: ")
    if side2.isdigit() and int(side2) > 0:
        side2 = int(side2)
        break
while True:
    side3 = input("Input third side: ")
    if side3.isdigit() and int(side3) > 0:
        side3 = int(side3)
        break

if side1 == side2 == side3:
    print("Equilateral triangle")
if side1 != side2 != side3:
    print("Equilateral triangle")
if side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles triangle")
