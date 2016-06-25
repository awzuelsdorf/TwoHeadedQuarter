#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double J(const double t) {
    int i;

    double sum = 0;

    for (i = 0; i < t; i += 1) {
        sum += 40000 * pow(1.05, i);
    }

    return sum;

}

double K(const double t) {
    int i;

    double sum = -155000;

    for (i = 0; i < t; i += 1) {
        sum += 60000 * pow(1.06, i);
    }

    return sum;
}

int main(int argc, char **argv) {
    size_t t = 0;

    //Assume that Karen and Joe will be able to work until their 72nd birthdays
    while (t <= 50 && J(t) >= K(t)) t += 1;

    if (t > 50 || J(t) >= K(t)) {
        puts("It is not worth it for Karent to go to business school.");
    }
    else if (J(t) < K(t)) {
        puts("It is worth it for Karen to go to business school.");
    }

    return EXIT_SUCCESS;
}
