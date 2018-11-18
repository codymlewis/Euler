import math
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


def sum_primes(n):
    i = prime_sum = 2
    while i < n:
        if is_prime(i):
            prime_sum += i
        i += 1
    return prime_sum


def is_prime(n):
    for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if (n % i) == 0:
            return False
    return True


if __name__ == "__main__":
    LIMIT = 2_000_000
    print("Started finding sum...")
    print(f"The sum of primes below {LIMIT} is {sum_primes(LIMIT)}")
