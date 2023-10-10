# Use the function from the previous task to simulate 1000 dice rolls and print the result. Calculate the number of times each number was rolled.
import random


def roll_dice():
    return random.randint(1, 6)


# Initialize a list of size 6 filled with zeros. Each entry corresponds a dice face.
results = [0, 0, 0, 0, 0, 0, 0]

for _ in range(1000):
    results[roll_dice()] += 1  

for i in range(1,6):
    print(f"The number {i} was rolled {results[i]} times")
