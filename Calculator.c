#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

float calculate(float a, char opt, float b);

int main(void) {
    float output;
    float n1, n2;
    char op;

    printf("Easy Calculator v1.0_gcc\n");
    printf("Copyright © 2021 Kazan All Rights Reserved.\n");

    while (true) {
        printf("Enter a two-numbers arithmetic (Ctrl-D to exit): ");
        int res = scanf("%f%c%f", &n1, &op, &n2);
        if (res != 3) {
            break;
        }

        output = calculate(n1, op, n2);
        if (isnan(output) == false) {
            printf("%.3f\n", output);
        } else {
            printf("Invalid input\n");
        }
    }

    printf("Thanks for use\n");

    return EXIT_SUCCESS;
}

float calculate(float a, char opt, float b) {
    switch (opt) {
    case '+':
        return a + b;
    case '-':
        return a - b;
    case '*':
        return a * b;
    case '/':
        if (b == 0) {
            return NAN;
        } else {
            return a / b;
        }
    default:
        return NAN;
    }
}
