import math

primes = []

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

a = 0
while a < 1000000:
    a = find_next_prime()

stringed_primes = ""
for prime in primes:
    stringed_primes += str(prime) + "\n"
outputfile = open("primes.txt", "w")
outputfile.write(stringed_primes)