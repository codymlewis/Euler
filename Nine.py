'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def find_triplet_product():
    a = 1
    b = 1
    c = 1000 - (a + b)
    while a < c:
        while c > 0:
            if (a**2 + b**2) == c**2:
                return a * b * c
            b += 1
            c -= 1
        a += 1
        b = a
        c = 1000 - (a + b)
    return -1

if __name__ == "__main__":
    print(f"The product of the Pythagorean triplet fitting a + b + c = 1000 is {find_triplet_product()}")
