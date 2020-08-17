"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

num = 600851475143
primes = []
factors = []
def find_next_prime():
    if not len(primes):
        primes.append(2)
        return 2
    if len(primes) == 1:
        primes.append(3)
        return 3
    biggest_prime = primes[len(primes) - 1]
    test_prime =  biggest_prime + 2
    while True:
        for prime in primes:
            if prime > round(math.sqrt(test_prime)):
                primes.append(test_prime)
                return test_prime
            if test_prime % prime == 0:
                test_prime += 2
                break

while num not in primes:
    biggest_prime = find_next_prime()
    while num % biggest_prime == 0:
        if num == biggest_prime:
            print(factors)
            print(biggest_prime)
            break
        num = num // biggest_prime
        factors.append(biggest_prime)
