"""
Quadratic Solver
Dakota Marosi
CS 1210
Program finds roots of a quadratic polynomial, if any
"""

import math

if __name__ == '__main__':
    
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    c = float(input("Enter value for c: "))


    def calc_discriminant(a, b, c):
        discriminant = (b ** 2 - (4 * a * c))
        return discriminant


    d = calc_discriminant(a, b, c)
    if d > 0:
        root_one = (-b + math.sqrt(d))/(2 * a)
        root_two = (-b - math.sqrt(d))/(2 * a)
        print(f"This equations two roots are {root_one:.3f} and {root_two:.3f}")
    elif d == 0:
        single_root = (-b / (2 * a))
        print(f"There is one real root to this equation {single_root:.3f}")
    else:
        print("There are no real roots to this equation.")
            
