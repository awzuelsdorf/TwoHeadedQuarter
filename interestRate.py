#! /usr/bin/env python

from carPayment import getMonthlyPayment

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
    #If your monthly payment is less than the amount
    #of interest your loan will accrue, then you will be
    #in debt forever.
    if (P - A) * (r / 100) >= A:
        return float("inf")

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

    r = getInterestRate(P, t, A)
    print("r (estimated): {0}".format(r))
    print("A (estimated): {0}".format(getMonthlyPayment(P, r, t)))
    print("A (exact): {0}".format(A))

    P = 3000
    A = 66
    r = 18

    t = getLoanTerm(P, r, A)
    print("t (estimated): {0}".format(t))
    print("A (estimated): {0}".format(getMonthlyPayment(P, r, t)))
    print("A (exact): {0}".format(A))

    t = getLoanTerm(P, r, 66, 0.1)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r, 66, 0.01)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r, 66, 0.001)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r, 66, 0.0001)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r, 50, 0.1)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r, 50, 0.01)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r, 50, 0.001)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r, 50, 0.0001)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r, 10, 0.1)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r, 10, 0.01)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r, 10, 0.001)
    print("t (for only paying the minimum payment): {0}".format(t))
    t = getLoanTerm(P, r, 10, 0.0001)
    print("t (for only paying the minimum payment): {0}".format(t))

    t = getLoanTerm(P, 0, 10, 0.0001)
    print("screwTest1: {0}".format(t))
    t = getLoanTerm(P, 10, 0, 0.0001)
    print("screwTest2: {0}".format(t))
    t = getLoanTerm(P, 0, 0, 0.0001)
    print("screwTest3: {0}".format(t))
    t = getLoanTerm(0, 10, 0, 0.0001)
    print("screwTest4: {0}".format(t))

if __name__ == "__main__":
    main()
