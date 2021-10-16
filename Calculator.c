#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>

float Cal(float a, char opt, float b);

int main(void) {
    float n1, n2, n;
    char op;
    
    // Program Title and copyright
    printf("%s", "Easy Calculator v1.0_gcc\n");
    printf("Copyright © 2021 Kazan All Rights Reserved.\n");
    
    printf("Enter a two-numbers arithmetic(Enter 0 and 0 to end): ");
    scanf("%f%c%f", &n1, &op, &n2);

    while (n1 != 0 && n2 != 0) { 
        
        n = Cal(n1, op, n2);
        if (n != 0 && n != -1) {
            printf("%.3f\n", n);
        }
        else if (n == FLT_MIN || n == FLT_MAX) {
            printf("%s\n", "Invalid iuput");
        }
        printf("Enter a two-numbers arithmetic(Enter 0 and 0 to end): ");
        scanf("%f%c%f", &n1, &op, &n2);
    }
    printf("%s\n", "Thanks for use");

    return 0;
}

float Cal(float a, char opt, float b) {
    float output;

    switch (opt)
    {
    case '+':
        output = a + b;
        break;
    case '-':
        output = a - b;
        break;
    case '*':
        output = a * b;
        break;
    case '/':
        if (b == 0) {
            output = FLT_MIN;
        }
        else {
            output = a / b;
        }
        break;
    default :
        output = FLT_MAX;
        break;
    }

    return output;
}