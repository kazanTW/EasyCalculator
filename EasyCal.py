#!/usr/bin/python

import sys
import tk as tk

def Cal(a, b, op):
    if op == '+':
        output = a + b
    elif op == '-':
        output = a - b
    elif op == '*':
        output = a * b
    elif op == '/':
        try:
            output = a / b
        except ZeroDivisionError:
            output = sys.float_info.min
    return output

def Cal_P():
    n1, opt, n2 = input("Enter a two-number operation(Enter 0 and 0 to end): ").split()
    N = Cal((float)(n1), (float)(n2), opt)

# Program Title and copyright
print("Easy Calculator v1.0_py3")
print("Copyright © 2021 Kazan All Rights Reserved.")
print("")

n1, opt, n2 = input("Enter a two-number operation(Enter 0 and 0 to end): ").split()

if ((float)(n1) == 0) and ((float)(n2) == 0):
    COND = False
else:
    COND = True

while COND == True:
    N = Cal((float)(n1), (float)(n2), opt)
    print(N)
    Cal_P()

    if ((float)(n1) == 0) and ((float)(n2) == 0):
        COND = False
    elif output == sys.float_info.min:
        print("Invalid input. Cannot divide 0.")
    else:
        Cal_P()

print("Thanks for use.")
sys.exit()