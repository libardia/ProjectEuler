# ======================================================================================================================
# PROBLEM 014:
#   The following iterative sequence is defined for the set of positive integers:
#
#   n -> n/2 (n is even)
#   n -> 3n + 1 (n is odd)
#
#   Using the rule above and starting with 13, we generate the following sequence:
#   13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
#   It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
#   proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#   Which starting number, under one million, produces the longest chain?
#
#   NOTE: Once the chain starts the terms are allowed to go above one million.
# ======================================================================================================================
# SOLUTION:
#   837799
# ======================================================================================================================
# NOTES:
#   Works, but takes ~87 seconds. I'm not quite sure how to trim this one down.
#
#   Update: User GarlicSauce on the PE problem discussion noted that you can skip checking all numbers in the chain
#   greater than the starting number, because their chains are sub-chains.
# ======================================================================================================================

import time

bound = int(input("Find the number less than n which produces the longest Collatz sequence: "))

start = time.clock()

longest = 0
answer = 0
for i in range(1, bound):
    n = i
    count = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        count += 1
    if count > longest:
        longest = count
        answer = i
    i += 1

end = time.clock()

print("\nInteger producing the largest Collatz sequence under {} is: {}, at {} steps".format(bound, answer, longest))
print("\nThat took {:.7f} seconds.".format(end-start))