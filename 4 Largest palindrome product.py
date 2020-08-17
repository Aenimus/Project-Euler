"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def reverse_string(input):
    return input[::-1]

def find_palindrome():
    a = 999
    b = 500
    n = 0
    x = 0
    y = 0
    for i in range(a, b, -1):
        for j in range(a, b, -1):
            num = i * j
            string = str(num)
            palindrome = reverse_string(string)
            if string == palindrome and n < num:
                n = num
                x = i
                y = j
        a -= 1
    print(f"{x} * {y} is {n}.")
    print(n)

find_palindrome()
