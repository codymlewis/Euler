import math
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
'''


def prime(n):
    # could cheat with SymPy, but that is not fun.
    i = 2
    prime_count = 1
    while prime_count < n:
        i += 1
        if is_prime(i):
            prime_count += 1
    return i


def is_prime(n):
    for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if (n % i) == 0:
            return False
    return True


if __name__ == "__main__":
    LIMIT = 10_001
    print("Started finding number...")
    print(f"The {LIMIT}th prime is {prime(LIMIT)}")
