# 1. Write a function called `find_primes` that takes in two integers a and b and returns a list of all the prime numbers between a and b (inclusive).
def find_primes(a: int, b: int):
    primes = []
    while a <= b:
        if is_prime(a):
            primes.append(a)
        a += 1
    return primes


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


print(find_primes(3, 20))
