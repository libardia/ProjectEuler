# ======================================================================================================================
# PROBLEM 001:
#   If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
#   multiples is 23.
#
#   Find the sum of all the multiples of 3 or 5 below 1000.
# ======================================================================================================================
# SOLUTION:
#   233168
# ======================================================================================================================
# NOTES:
#   Taking advantage of the fact that the sum of all integers up to n is n(n+1)/2, and therefore m * n(n+1)/2 is the sum
#   of the first n multiples of m, we can take all the multiples of 3 up to our target, add all the multiples of 5 up to
#   our target, and subtract all the multiples of 15 up to our target (because they have been counted twice). "//" is
#   used to perform floor() in the same step as the division and also to keep the values as integers as opposed to
#   floats. This is now O(1) for all inputs.
# ======================================================================================================================
import time

target = int(input("Sum multiples of 3 and 5 less than: "))

start = time.clock()

a = (target - 1) // 3
b = (target - 1) // 5
c = (target - 1) // 15

total = (3*a*(a+1) + 5*b*(b+1) - 15*c*(c+1)) // 2

end = time.clock()

print(f"Total of all multiples of 3 and 5 less than {target} is {total}")
print(f"\nThat took {end-start:.7f} seconds.")