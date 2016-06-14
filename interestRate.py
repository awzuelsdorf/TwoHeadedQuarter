#! /usr/bin/env python

from carPayment import getMonthlyPayment

def getTotalMoneyPaid(P, r, t):
    return t * getMonthlyPayment(P, r, t) 

def getInterestRate(P, t, A, tolerance=0.0009765625):
    r1 = 0.0001
    r2 = 100.0
    r3 = 0.0
    f = carPaymentRooted

    done = False

    while not done:
        r3 = (r1 + r2) / 2

        if f(P, r3, t, A) * f(P, r1, t, A) < 0:
            r2 = r3
        else:
            r1 = r3
        done = abs(r1 - r2) < 2 * tolerance

    return r3

def getLoanTerm(P, r, A, maxTime=2400, tolerance=0.0009765625):
    f = carPaymentRooted
    previous = None
    current = None

    done2 = False
    done1 = False

    t1 = 0.0001
    t2 = maxTime
    t3 = 0.0

    while not done2:
        t3 = (t1 + t2) / 2

        if f(P, r, t3, A) * f(P, r, t1, A) < 0:
            t2 = t3
        else:
            t1 = t3
        done2 = abs(t1 - t2) < 2 * tolerance

    if f(P, r, t3, A) >= tolerance:
        try:
            return getLoanTerm(P, r, A, maxTime * 2, tolerance)
        except:
            return float("inf")
    else:
        return t3

def carPaymentRooted(P, r, t, A):
    return getMonthlyPayment(P, r, t) - A

def main():
    P = 5000
    A = 100
    t = 60

    r = getInterestRate(P, t, A) * 12
    print("r (estimated): {0}".format(r))
    print("A (estimated): {0}".format(getMonthlyPayment(P, r / 12.0, t)))
    print("A (exact): {0}".format(A))

    P = 3000
    A = 66
    r = 18

    t = getLoanTerm(P, r / 12.0, A)
    print("t (estimated): {0}".format(t))
    print("A (estimated): {0}".format(getMonthlyPayment(P, r / 12.0, t)))
    print("A (exact): {0}".format(A))

    t = getLoanTerm(P, r / 12.0, 66, 0.1)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r / 12.0, 66, 0.01)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r / 12.0, 66, 0.001)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r / 12.0, 66, 0.0001)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r / 12.0, 50, 0.1)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r / 12.0, 50, 0.01)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r / 12.0, 50, 0.001)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r / 12.0, 50, 0.0001)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r / 12.0, 10, 0.1)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r / 12.0, 10, 0.01)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r / 12.0, 10, 0.001)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r / 12.0, 10, 0.0001)
    print("t (for only paying the minimum payment): {0}".format(t))

    t = getLoanTerm(P, 10 / 12.0, 0)
    print("screwTest1: {0}".format(t))
    t = getLoanTerm(P, 10 / 12.0, 0)
    print("screwTest2: {0}".format(t))
    t = getLoanTerm(P, 0 / 12.0, 0) #TODO: Fix this!
    print("screwTest3: {0}".format(t))
    t = getLoanTerm(0, 11 / 12.0, 0) #TODO: Fix this!
    print("screwTest4: {0}".format(t))

    P = 15000.0
    r = 9.0
    t = 60.0

    M = getTotalMoneyPaid(P, r / 12.0, t)

    print("Total cost of financing a ${0} vehicle at {1}% APR for {2} months is ${3}".format(P, r, t, M))

    print("Total cost of 15-year mortgage: ${0}".format(getTotalMoneyPaid(140000, 7.0 / 12.0, 15 * 12.0)))
    print("Total cost of 30-year mortgage: ${0}".format(getTotalMoneyPaid(140000, 7.0 / 12.0, 30 * 12.0)))

    print("The $16000 offer will cost ${0} total".format(getTotalMoneyPaid(16000, 5.0 / 12.0, 12.0 * 4.0)))
    print("The $15000 offer will cost ${0} total".format(getTotalMoneyPaid(15000, 5.5 / 12.0, 12.0 * 4.0)))

    print("The $2400 offer will cost ${0} total".format(getTotalMoneyPaid(2400, 15.0 / 12.0, 12.0 * 3.0)))
    print("The $2995 offer will cost ${0} total".format(getTotalMoneyPaid(2995, 0.0 / 12.0, 12.0 * 3.0)))

if __name__ == "__main__":
    main()
