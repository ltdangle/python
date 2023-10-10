# Write a function that simulates a dice roll and returns the result from 1 to 6. Use random module
import random


def roll_dice():
   return random.randint(1, 6)

print(roll_dice())
