# ======================================================================================================================
# PROBLEM 015:
#   Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly
#   6 routes to the bottom right corner.
#
#   How many such routes are there through a 20x20 grid?
# ======================================================================================================================
# SOLUTION:
#   137846528820
# ======================================================================================================================
# NOTES:
#   Solution aquired in ~0.0000377 seconds.
#
#   I actually managed to discover on my own that the answer for any n x n grid is the (n+1)th n-simplex number. Now, I
#   didn't know what those were at the time: they are the higher dimentional equivalents of triangle numbers. If a
#   triange number is dimension 2, a tetrahedral number is dimension 3, and an n-simplex number is of dimension n. Each
#   n-simplex number is the sum of the first n (n-1)-simplex numbers, so the nth tetrahedral number is the sum of the
#   first n triangle numbers. Using that, I derived a recursive algorithm to find them:
#
#       simplex(d, n) = | when d = 2: n(n+1)/2
#                       | when n = 1: 1
#                       |  otherwise: sum with i from 1 to n of triseq(d-1, i)
#
#   I chose d = 2 for the first primitive case because it was the smallest one that I knew the formula for. I knew there
#   was a formula for the nth tetrahedral number, but I didn't know exactly what it was. This worked, but it was much
#   too slow. The number of paths of the type the problem demands for an n x n grid is triseq(n, n+1), and for n=17, it
#   took about 320 seconds to compute, while n=16 took about 80 and n=15 took about 20. It was clearly increasing much
#   too quickly to handle. At that rate calculating n=20 would take over five and a half hours.
#
#   I was looking up the formula for tetrahedral numbers after this and stumbled across simplex series, and found that
#   the formula for the nth d-simplex number is (n+d-1 choose d). Instantly, I could collapse my function to no longer
#   use recursion, and instead just a few factorials, each of which is just one for loop. This brought the time down
#   from five and a half hours to less than a ten-thousandth of a second, reduced by a factor of ~5.5*10^8. Amazing!
#
#   One last note: Working on another project, I realized I could keep a cache of the results of the function with
#   certain inputs for recursive functions. Using that strategy here, the recursive version of the function now runs in
#   ~0.002 seconds. Slower than the simplex version, But much more bearable. It doesn't start getting over 20 seconds
#   until a grid with sidelength 400. Of course, the simplex version calculates sidelength 400 in less than a second,
#   and uses much, much less space because of how big the cache gets... but I'm very happy with the improvement.
# ======================================================================================================================

import time
from math import factorial as fact

# ======================================================================================================================

def simplex(d, n):
    # Do it the easy way!
    return choose(n + d - 1, d)

def choose(n, k):
    # Formula for n choose k
    return fact(n)/(fact(n-k) * fact(k))

cache = dict()
def recursive(d, n):
    # Handle all the primitive cases
    if d == 2:
        return n*(n+1)/2
    if d == 1:
        return n
    if n == 1:
        return 1

    # If we aren't in a primitive case, have we done this one before?
    if (d,n) in cache:
        return cache[(d,n)]

    # If not, calculate it, and put it in the cache.
    total = 0
    for i in range(1, n+1):
        total += recursive(d-1, i)
    cache[(d,n)] = total
    return total

# ======================================================================================================================

print(simplex())

n = int(input("Side length of grid: "))

# Which method would you like to use?
f = recursive
#f = simplex

start = time.clock()

paths = f(n, n+1)

end = time.clock()

print("\nNumber of paths through a {}x{} grid is {}".format(n, n, int(paths)))
print("\nThat took {:.7f} seconds.".format(end-start))
