#! /usr/bin/env python

import sys
from numpy import arange

#P = the amount of money that you are going to borrow.
#r = the annual percentage rate (APR).
#t = the number of months in the loan's term (how long
#you are going to take to pay off the loan).
def getMonthlyPayment(P, r, t):
    if r < 0 or P < 0 or t < 0:
        raise ValueError("Invalid parameters: A = {0}, r = {1}, t = {2}. All parameters must be at least zero.".format(P, r, t))
    elif r != 0: #TODO: Figure out a better way to
        #determine whether r is zero.
        return P * (r / 100.0 / 12.0 * ((1 + r / 100.0 / 12.0) ** t)) / (((1 + r / 100.0 / 12.0) ** t) - 1)
    else:
        return 1.0 * P / t

#P = the most you are willing to pay per month for this
#car (the maximum monthly payment)
#r = the annual percentage rate
#t = the number of months in the loan's term.
def getMaximumCarPrice(P, r, t):
    if P < 0 or r < 0 or t < 0:
        raise ValueError("Invalid parameters: P = {0}, r = {1}, t = {2}. All parameters must be at least zero.".format(P, r, t))
    elif r != 0: #TODO: Figure out a better way to
        #determine whether r is zero.
        raise BaseException("Not implemented yet!")
    else:
        raise BaseException("Not implemented yet!")

def main():
    for r in arange(0, 10 + 0.5, 0.5):
        for t in range(2, 6 + 1, 1):
            sys.stdout.write(str(getMonthlyPayment(1000, r, 12 * t)) + " ")
        sys.stdout.write("\n")

    print(getMonthlyPayment(13687, 4.65, 60))

if __name__ == "__main__":
    main()
