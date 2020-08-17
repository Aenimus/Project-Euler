"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

import re

with open("primes.txt") as p:
    primes = set(p.readlines())

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
trimmed_primes = []
filtered_primes = []
fil = re.compile("(\\d).*\\1.*\\1")
for prime in primes:
    prime = prime.strip("\n")
    if len(prime) == 6:
        trimmed_primes.append(prime)
trimmed_primes.sort()
filtered_primes = [p for p in trimmed_primes if fil.match(p)]

def find_prime_family():
    for prime in trimmed_primes:
        succ = 0
        fail = 0
        smallest_family_prime = 0
        for i in range(4):
            for j in range(i+1, 5):
                for k in range(j+1, 6):
                    a = prime
                    for num in numbers:
                        if i == 0:
                            if num == "0":
                                continue
                            a = num + a[i+1:j] + num + a[j+1:k] + num + a[k+1:]
                        else:
                            a = a[:i-1] + num + a[i+1:j] + num + a[j+1:k] + num + a[k+1:]
                        if a == prime:
                            continue
                        if a in filtered_primes:
                            succ += 1
                            if (succ == 1):
                                smallest_family_prime = a
                            print(f"{succ}: {a}")
                        else:
                            fail += 1
                        if fail > 2:
                            succ = 0
                            fail = 0
                            break
                        if succ > 7:
                            print(smallest_family_prime)
                            return
                    #print(f"{i}, {j}, {k}")

find_prime_family()