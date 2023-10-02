# 3. Write a function that caluculate [Fibonacci series](https://en.wikipedia.org/wiki/Fibonacci_sequence).
# The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers.
# The first two numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth number is 1 + 2 = 3, and so on.
# Number of iterations should be taken from user input.


def fibonacci(n: int):
    fib = [1, 1]
    i = 2
    while i < n:
        fib.append(fib[i - 2] + fib[i - 1])
        i = i + 1

    return fib


while True:
    num = input("Enter number larger than 2: ")
    if num.isdigit() and int(num) > 2:
        num = int(num)
        break

print(fibonacci(num))
