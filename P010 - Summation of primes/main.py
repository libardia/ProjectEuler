# ======================================================================================================================
# PROBLEM 010:
#   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#   Find the sum of all the primes below two million.
# ======================================================================================================================
# SOLUTION:
#   142913828922
# ======================================================================================================================
# NOTES:
#   This was kind of a cheaty way to solve this. I just pulled a primality test off of Wikipedia. And not just the
#   algorithm; it was actually implemented in python on the page. Ugh. The only real difference between this and my
#   incredibly slow implementation is the range. This one is from 5 to sqrt(n) + 1 with steps of 6. That's certainly
#   much more efficient than my range: 3 to n/2 in steps of 2. Solved in just over twelve seconds.
# ======================================================================================================================

import time

# ================================================

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# ================================================

target = int(input("Find sum of primes below: "))

start = time.clock()

total = 0

if target > 2:
    total = 2
    for i in range(3, target, 2):
        if is_prime(i):
            total += i

end = time.clock()

print(total)
print("\nThat took {:.7f} seconds.".format(end-start))