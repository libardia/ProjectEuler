# ======================================================================================================================
# PROBLEM 003:
#   The prime factors of 13,195 are 5, 7, 13 and 29.
#
#   What is the largest prime factor of the number 600,851,475,143 ?
# ======================================================================================================================
# SOLUTION:
#   6857
# ======================================================================================================================
# NOTES:
#   This is the result of a lot of time thinking about this. As this is my second time doing PE, I had a lot of trouble
#   with this problem the first time, but it interested me, and I came up with this algorithm to find prime factors.
# ======================================================================================================================

import time

n = int(input("Number to prime factorize: "))

start = time.clock()

factors = []
f = 2

while n > 1:
    while n % f == 0:
        factors += [f]
        n /= f
    if f > 2:
        f += 2
    else:
        f += 1

end = time.clock()

print(factors)
print("\nThat took {:.7f} seconds.".format(end-start))