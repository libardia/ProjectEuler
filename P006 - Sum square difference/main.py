# ======================================================================================================================
# PROBLEM 006:
#   The sum of the squares of the first ten natural numbers is,
#
#   12 + 22 + ... + 102 = 385
#
#   The square of the sum of the first ten natural numbers is,
#
#   (1 + 2 + ... + 10)2 = 552 = 3025
#
#   Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#   3025 − 385 = 2640.
#
#   Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the
#   sum.
# ======================================================================================================================
# SOLUTION:
#   25164150
# ======================================================================================================================
# NOTES:
#   I took the formula for the sum of the first n natural numbers, squared it, and subtracted the equivalent formula for
#   the first n squares and simplified. The formula here is the solution to the problem for the first n natural numbers.
# ======================================================================================================================

import time

n = int(input("Find the sum square difference of the first n natural numbers: "))

start = time.clock()

#   n(n**2 - 1)(3n + 2)     Gives the difference between the sum of the squares and square of the sum of the first n
#   -------------------     natural numbers.
#           12
result = (n * (n**2 - 1) * (3*n + 2)) // 12

end = time.clock()

print(result)
print("\nThat took {:.7f} seconds.".format(end-start))