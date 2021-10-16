#!/usr/bin/python

import sys


def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        raise ValueError('Invalid operator {}'.format(op))


def prompt_and_calculate():
    n1, opt, n2 = input(
        "Enter a two-number operation(Enter 0 and 0 to end): ").split()
    return calculate(float(n1), float(n2), opt)


# Program Title and copyright
print("Easy Calculator v1.0_py3")
print("Copyright © 2021 Kazan All Rights Reserved.")
print("")

n1, opt, n2 = input(
    "Enter a two-number operation(Enter 0 and 0 to end): ").split()

if ((float)(n1) == 0) and ((float)(n2) == 0):
    COND = False
else:
    COND = True

while COND == True:
    N = calculate((float)(n1), (float)(n2), opt)
    print(N)
    prompt_and_calculate()

    if ((float)(n1) == 0) and ((float)(n2) == 0):
        COND = False
    elif output == sys.float_info.min:
        print("Invalid input. Cannot divide 0.")
    else:
        prompt_and_calculate()

print("Thanks for use.")
sys.exit()

