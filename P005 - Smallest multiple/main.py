# ======================================================================================================================
# PROBLEM 005:
#   2,520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# ======================================================================================================================
# SOLUTION:
#   232792560
# ======================================================================================================================
# NOTES:
#   Using the analysis method (picking the largest number of similar prime factors), generalized to the first n natural
#   numbers, and Python's freakishly huge storage for integers, this can get the smallest number for a stupidly big
#   amount of consecutive natural numbers. The largest I've tried was 5000; the solution was over 2,150 digits long. It
#   took just barely over a second to compute.
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

# ================================================
n = int(input("Find smallest number that can be divided by the numbers 1 to: "))

start = time.clock()

# find only the necessary factors
allfactors = []
i = 2
isin = False
while i <= n:
    factors = getfactors(i)
    if len(allfactors) == 0:
        allfactors = factors
    else:
        for prime,power in factors:
            for j in range(len(allfactors)):
                if prime == allfactors[j][0]:
                    isin = True
                    if power > allfactors[j][1]:
                        allfactors[j][1] = power
                    break
            if not isin:
                allfactors.append([prime,power])
            isin = False
    i += 1

# get the number
total = 1
for prime,power in allfactors:
    total *= prime**power

end = time.clock()

print("It's factors are: {}".format(allfactors))
print("The answer is: {}".format(total))
print("\nThat took {:.7f} seconds.".format(end-start))