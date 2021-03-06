# ======================================================================================================================
# PROBLEM 016:
#   2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#   What is the sum of the digits of the number 2^1000?
# ======================================================================================================================
# SOLUTION:
#   1366
# ======================================================================================================================
# NOTES:
#   Took ~0.0002 seconds.
#   This question was kinda terrible. Nothing more than the obvious solution is necessary.
# ======================================================================================================================

import time

# ======================================================================================================================

# ======================================================================================================================

n = int(input("Sum of digits of 2^n: "))

start = time.clock()

total = 0
for x in str(2**n):
    total += int(x)

end = time.clock()

print("\nResult is {}".format(total))
print("\nThat took {:.7f} seconds.".format(end-start))
