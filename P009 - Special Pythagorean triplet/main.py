# ======================================================================================================================
# PROBLEM 009:
#   A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#   a^2 + b^2 = c^2
#
#   For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
#   There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#   Find the product abc.
# ======================================================================================================================
# SOLUTION:
#   31875000
# ======================================================================================================================
# NOTES:
#   I'm lucky to still have my notes lying around from when I did this problem the first time, because it took me a lot
#   of thinking to come up with this algorithm.
# ======================================================================================================================

import time

target = int(input("Find the first Pythagorean triplet where a + b + c equals: "))

start = time.clock()

a = 2
b = 3
c = target - a - b

exists = False
while a < c:
    while b < c:
        if a**2 + b**2 == c**2:
            exists = True
        if exists:
            break
        else:
            b += 1
            c -= 1
    if exists:
        break
    else:
        a += 1
        b = a+1
        c = target - a - b

end = time.clock()

if exists:
    print("{0}^2 + {1}^2 = {2}^2\n{0} * {1} * {2} = {3}".format(a, b, c, a*b*c))
else:
    print("There is no Pythagorean triplet where a + b + c = {}.".format(target))
print("\nThat took {:.7f} seconds.".format(end-start))