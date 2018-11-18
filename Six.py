import math
'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''


def find_sum(n):
    sigma = 0
    square_sigma = 0
    for i in range(1, n + 1):
        sigma += i
        square_sigma += i**2
    return (sigma**2) - square_sigma


if __name__ == "__main__":
    LIMIT = 100
    SIGMA = find_sum(LIMIT)
    print(f"The difference between the sum of the squares of the first " +
          f"{LIMIT} natural numbers is {SIGMA} and the square of the sum " +
          f" is {SIGMA**2}")
