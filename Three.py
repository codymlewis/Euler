import math
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''
def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if (n % i) == 0:
            return False
    return True


def find_biggest_prime_factor(n):
    for i in range(int(math.sqrt(n)), 1, -1):
        if is_prime(i) and (n % i) == 0:
            return i
    return 1

if __name__ == "__main__":
    LIMIT = 600_851_475_143
    print("Started calculating...")
    print(f"The biggest prime factor of {LIMIT} is {find_biggest_prime_factor(LIMIT)}")
