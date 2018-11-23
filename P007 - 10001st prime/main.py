# ======================================================================================================================
# PROBLEM 007:
#   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#   What is the 10,001st prime number?
# ======================================================================================================================
# SOLUTION:
#   104743
# ======================================================================================================================
# NOTES:
#   Takes about 12.9929 seconds.
#
#   UPDATE: Checkinng up to n//3 + 1 is unnecessary. Checking up to sqrt(n) is the minimum. This change cuts the time
#   from 12.9929 to ~0.3 seconds.
# ======================================================================================================================

import time
from math import floor

# ================================================

def primecheck(n):
    if n == 2: return True
    if n % 2 == 0: return False
    #for i in range(3, (n//3)+1, 2):
    for i in range(3, floor(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# ================================================

target = int(input("Find the nth prime, where n is: "))

start = time.clock()

curprime = 2

if target != 1:
    numprimes = 1
    i = 3
    curprime = 0
    while numprimes < target:
        if primecheck(i):
            numprimes += 1
            curprime = i
        i += 2

end = time.clock()

print(curprime)
print("\nThat took {:.7f} seconds.".format(end-start))