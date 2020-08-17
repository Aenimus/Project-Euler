"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

numbers = [11,12,13,14,15,16,17,18]
done = False
i = 2
c = 0
b = 0
while not done:
    a = 19 * i
    b = 20 * a
    print(b)
    for num in numbers:
        if b % num == 0:
            c = b // num
            if c % 2 == 0:
                if num == 18:
                    done = True
                    print(b)
                continue
        else:
            i += 2
            break
