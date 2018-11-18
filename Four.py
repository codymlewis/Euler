'''
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def find_palindrome():
    '''
    Find the palindromic number.
    '''
    i = 999
    while i > 99:  # O(n^2)
        j = 999
        while j > 99:
            if is_palindrome(i * j):
                return i * j
            j -= 1
        i -= 1
    return -1


def is_palindrome(n):
    '''
    Check if a given number is palindromic.
    '''
    possible_pal = str(n)
    for i in range(int(len(possible_pal) / 2)):
        if possible_pal[i] != possible_pal[len(possible_pal) - (i + 1)]:
            return False
    return True


if __name__ == "__main__":
    print(f"The biggest palindromic number that is a product of 2 three " +
          f"digit numbers is {find_palindrome()}")
