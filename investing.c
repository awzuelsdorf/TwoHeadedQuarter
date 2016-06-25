#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>

#define DEFAULT_TOLERANCE 0.0009765625

double paymentSize(const double finalAmt, const size_t periods,
                   const double interestRate) {

    assert(interestRate < 1);

    double sum = 0;
    size_t period;

    for (period = 0; period < periods; period += 1) {
        sum += pow(1 + interestRate, period);
    }

    return finalAmt / sum;
}

double finalAmount(const double paymentSize, const size_t periods,
                   const double interestRate) {
    double sum = 0;
    size_t period;

    for (period = 0; period < periods; period += 1) {
        sum += paymentSize * pow(1 + interestRate, period);
    }
    
    return sum;
}

double rateNeeded(const double finalAmt, const size_t periods,
                  const double paymentSize) {

    double x3, x2, x1, f1, f3, tol;

    //Check for 0% interest.
    if (finalAmt <= paymentSize) {
        return 0;
    }

    tol = DEFAULT_TOLERANCE * 2;

    x2 = 100;
    x1 = 0.001;
    x3 = 0;
 
    do {
       x3 = (x1 + x2) / 2;

       f3 = finalAmount(paymentSize, periods, x3 / 100.0) - finalAmt;
       f1 = finalAmount(paymentSize, periods, x1 / 100.0) - finalAmt;

       if (f3 * f1 < 0) {
           x2 = x3;
       }
       else {
           x1 = x3;
       }
    } while (abs(x1 - x2) >= tol);

    return x3 / 100.0;
}

int main(int argc, char **argv) {
    printf("Final amount: %f\n", finalAmount(12 * 100, 5, 0.06));
    printf("Final amount: %f\n", finalAmount(12 * 50, 25, 0.06));
    printf("Monthly payment amount: %f\n", paymentSize(500000, 20, 0.08) / 12);
    printf("Monthly payment amount: %f\n", paymentSize(700000, 40, 0.06) / 12);
    printf("Interest rate: %f\n", rateNeeded(500000, 20, 600 * 12));
    printf("Final amount: %f\n", finalAmount(600 * 12, 20, rateNeeded(500000, 20, 12 * 600)));
    printf("Monthly payment amount: %f\n", paymentSize(600000, 30, 0.06) / 12);

    return EXIT_SUCCESS;
}
