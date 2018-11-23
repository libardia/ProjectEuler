# ======================================================================================================================
# PROBLEM 017:
#   If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
#   letters used in total.
#
#   If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be
#   used?
# ======================================================================================================================
# SOLUTION:
#   21124
# ======================================================================================================================
# NOTES:
#   At first I thought this problem was stupid; it isn't math, it's only tangentially related because we're summing
#   things. And generating the english representation of the numbers 1 to 1000 was pretty easy. The fun came when I was
#   trying to create a recursive algorithm to give me any arbitrary number (as long as I had the suitable word for the
#   greatest power of 1000). That proved to be a really interesting problem. If you've been looking at my other
#   solutions, I really like recursion. I took advantage of every pattern in english numbers as I could to create an
#   algorithm that worked in groups of three digits, and I'm quite happy with the result. It doesn't catch everything;
#   there are some quirks of higher order numbers that it misses (i.e., you would probably say 1050 as "one thousand
#   and fifty," and while 'and's are taken into account, not here - my function returns "one thousand, fifty.") and some
#   that may just be my personal preference (i.e., for six-digit numbers and greater, only the last group of three gets
#   an 'and' - "654,321" becomes "six hundred fifty-four thousand, three hundred and twenty-one"). It's extremely
#   complicated, and I love it. I left a testing mode in the final product just to play around with it.
# ======================================================================================================================

import time

# ================================================

onetoninewords = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
onetonine      = [ 0,  3,     3,     5,       4,      4,      3,     5,       5,       4    ]
# zero is special here because you don't say them in the number except when it's zero itself. Having a (number) zero
# and an empty string here will prevent it from being counted.


tentonineteenwords = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tentonineteen      = [ 3,     6,        6,        8,          8,          7,         7,         9,           8,          8        ]

twentytoninetywords = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
twentytoninety      = [ 6,        6,        5,       5,       5,       7,         6,        6      ]

hundredword = "hundred"
hundred = 7

powersofthousandwords = ["thousand", "million", "billion", "trillion"]
powersofthousand      = [ 8,          7,         7,         8        ]

def lettersin(x, useand = True):
    xint = int(x)
    xstr = str(xint)

    if xint == 0: # is exactly zero
        return 4, "zero"
    elif xint < 10: # One digit and not zero
        return onetonine[xint], onetoninewords[xint]
    elif xint < 20: # Two digits and <20
        return tentonineteen[xint-10], tentonineteenwords[xint-10]
    elif xint < 100: # Two digits and >=20
        a = int(xstr[0])-2
        b = int(xstr[1])
        return \
            twentytoninety[a] + onetonine[b], \
            twentytoninetywords[a] + ("" if onetonine[b] == 0 else "-" + onetoninewords[b])
    elif xint < 1000: # Three digits
        a = lettersin(xstr[0])
        b = lettersin(xstr[1:])
        bzero = b[1] == "zero"

        if bzero:
            return \
                a[0] + hundred, \
                a[1] + " " + hundredword
        else:
            return \
                a[0] + hundred + (3 if useand else 0) + b[0], \
                a[1] + " " + hundredword + (" and " if useand else " ") + b[1]
    else: # >=1000
        if len(xstr) % 3 != 0:
            xstr = ("0" * (3 - (len(xstr) % 3))) + xstr
        mag = (len(xstr) // 3) - 2
        a = lettersin(xstr[:3], False)
        b = lettersin(xstr[3:], mag == 0)
        bzero = b[1] == "zero"
        return \
            a[0] + powersofthousand[mag] + (0 if bzero else b[0]), \
            a[1] + " " + powersofthousandwords[mag] + ("" if bzero else ", " + b[1])


# ================================================

print("NOTE: In test mode, enter any negative number to quit.")
mode = input("Enter T to go to test mode, S to solve the problem: ")
print()

while mode == "t" or mode == "T":
    i = input("i=")
    if int(i) < 0:
        exit(0)
    result = lettersin(i)
    print("'{}'\n{} letters\n".format(result[1], result[0]))

n = input("Sum the number of letters from one to: ")
total = 0

start = time.clock()

for i in range(int(n)):
    result = lettersin(i+1)
    total += result[0]

end = time.clock()

print("\nTotal number of letters in the numbers 1 to {} is {}".format(n, total))
print("\nThat took {:.7f} seconds.".format(end-start))