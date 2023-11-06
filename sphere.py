"""
Sphere
Dakota Marosi
CS 1210
Program calculates the volume and surface area of a sphere
"""

import math

def surface_area(radius):
    x = (4 * math.pi * (radius**2))
    return x

def volume(radius):
    y = ((4/3) * math.pi * (radius**3))
    return y

get_radius = float(input("What is the radius of the circle? "))
radius_to_surface_area = surface_area(get_radius)
radius_to_volume = volume(get_radius)
print(f"The sphere's volume is {radius_to_volume:.2f}")
print(f"The sphere's surface area is {radius_to_surface_area:.2f}")
