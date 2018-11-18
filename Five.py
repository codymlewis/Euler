'''
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''


def find_number():
    n = 1
    while True:  # \Theta(n) where n is |N|
        for i in range(1, 21):
            if (n % i) != 0:
                break
            if i is 20:
                return n
        n += 1

if __name__ == "__main__":
    print("Started finding number...")
    print(f"The smallest positive number that is evenly divisible by all of " +
          f" [1, 20] is {find_number()}")
