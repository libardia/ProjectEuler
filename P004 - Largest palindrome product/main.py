# ======================================================================================================================
# PROBLEM 004:
#   A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
#   is 9009 = 91 * 99.
#
#   Find the largest palindrome made from the product of two 3-digit numbers.
# ======================================================================================================================
# SOLUTION:
#   906609
# ======================================================================================================================
# NOTES:
#   Wow, this same algorithm took 20s on my last attempt using C++. In Python, it took 0.1s. I did improve it a little,
#   but even before I did it took 0.4s. I don't know what was going on in C++.
# ======================================================================================================================

import time

# ================================================

def palcheck(n):
    forward = str(n)
    reverse = forward[::-1]
    return forward == reverse

# ================================================

d = int(input("Find the largest palindromic product of two n-digit numbers, where n is: "))

start = time.clock()

# Get the relevant numbers
n = ""
lowerbound = ""
for i in range(d):
    if i == 0:
        lowerbound += "1"
    else:
        lowerbound += "0"
    n += "9"
n = int(n)
lowerbound = int(lowerbound)

# Do the thing
a = b = n
largest = 0
fa = 0
fb = 0

while a >= lowerbound:
    while b >= lowerbound:
        candidate = a*b
        if candidate > largest:
            if palcheck(candidate):
                largest = candidate
                fa = a
                fb = b
        b -= 1
    a -= 1
    b = a
    #if a % 100 == 0: print("{}%".format(100*(1-((a-lowerbound)/(n-lowerbound)))))

end = time.clock()

print("{} * {} = {}".format(fa, fb, largest))
print("\nThat took {:.7f} seconds.".format(end-start))