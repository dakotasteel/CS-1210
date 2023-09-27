"""
Quadratic Solver
Dakota Marosi
CS 1210
Program finds roots of a quadratic polynomial, if any
"""

import math

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))


def calc_discriminant(x, y, z):
    discriminant = (y ** 2 - (4 * x * z))
    return discriminant


d = calc_discriminant(a, b, c)
if d > 0:
    root_one = (-b + math.sqrt(d))/(2 * a)
    root_two = (-b - math.sqrt(d))/(2 * a)
    print(f"The two roots of this equation are \
          {root_one:.3f}  and  {root_two:.3f}")
elif d == 0:
    single_root = (-b / (2 * a))
    print(f"There is one real root to this equation {single_root:.3f}")
else:
    print("There are no real roots to this equation.")
        
