"""
Temp table
Dakota Marosi
CS 1210
Program produces a temperature table based on inputted degrees in F
"""

import math

def f_to_c(f):
    c = ((f-32) * (5/9))
    return c

get_f = float(input("Enter temperature in degrees F: "))
f_minus_ten = get_f - 10
f_plus_ten = get_f + 10

print("Fahrenheit      Celsius")
print(f"{get_f-10:>10} {(f_to_c(f_minus_ten)):>12.1f}")
print(f"{get_f:>10} {(f_to_c(get_f)):>12.1f}")
print(f"{get_f+10:>10} {f_to_c(f_plus_ten):>12.1f}")
