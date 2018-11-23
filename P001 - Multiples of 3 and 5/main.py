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
#   This was an attempt to only add numbers that I was sure fit the pattern. It's very specific unfortunately and I have
#   since read the overview and they have a much more elegant and efficient version of this solution. Damn. But I'm sure
#   that will be the case will all problems.
# ======================================================================================================================
import time

target = int(input("Sum multiples of 3 and 5 less than: "))

start = time.clock()

total = 0
current = 0

steps = [3, 2, 1, 3, 1, 2, 3]
istep = 0

while current < target:
    total += current
    current += steps[istep]
    istep = (istep + 1) % len(steps)

end = time.clock()

print("Total of all multiples of 3 and 5 less than {} is {}".format(target, total))
print("\nThat took {:.7f} seconds.".format(end-start))