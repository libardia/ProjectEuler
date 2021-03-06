# ======================================================================================================================
# PROBLEM 012:
#   The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
#   1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
#       1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#   Let us list the factors of the first seven triangle numbers:
#
#        1: 1
#        3: 1,3
#        6: 1,2,3,6
#       10: 1,2,5,10
#       15: 1,3,5,15
#       21: 1,3,7,21
#       28: 1,2,4,7,14,28
#
#   We can see that 28 is the first triangle number to have over five divisors.
#
#   What is the value of the first triangle number to have over five hundred divisors?
# ======================================================================================================================
# SOLUTION:
#   76576500
# ======================================================================================================================
# NOTES:
#   This solution takes ~10 seconds on my machine. I spent a REALLY long time trying to find a n easy way to get the
#   number of divisors of a number given it's prime factorization. I was doing frigging statistics to find the
#   combinations of the primes, but I couldn't get anywhere. Eventually I cracked and searched it; apparently just
#   adding one to each of the exponents and multiplying those together gives the number of divisors. Damn it.
# ======================================================================================================================

import time

# ================================================

def getfactors(n):
    factors = []
    f = 2
    i = -1
    first = True

    while n > 1:
        while n % f == 0:
            if first:
                factors.append([f, 1])
                i += 1
                first = False
            else:
                factors[i][1] += 1
            n /= f
        f += 1
        first = True

    return factors

def getnumdivs(n):
    factors = getfactors(n)
    total = 1
    for pair in factors:
        total *= pair[1] + 1
    return total

# ================================================

n = int(input("Get the first triangle number with more than n divisors: "))

start = time.clock()
result = 1
i = 1
divs = 0

while True:
    divs = getnumdivs(result)
    #print("{}: {}".format(result, divs))
    if divs > n: break
    i += 1
    result += i
end = time.clock()

print("{} has {} divisors.".format(result, divs))
print("\nThat took {:.7f} seconds.".format(end-start))