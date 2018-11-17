'''
If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
def find_sum(multiples, n):
    sigma = 0
    for i in range(n):
        for m in multiples:
            if (i % m) == 0:
                sigma += i
                break
    return sigma


if __name__ == "__main__":
    MULTIPLES = [3, 5]
    LIMIT = 1000
    print(f"The sum of the multiples {MULTIPLES} up to " +
            f"{LIMIT} is {find_sum(MULTIPLES, LIMIT)}")
