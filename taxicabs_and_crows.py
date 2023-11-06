"""
Taxicabs and crows
Dakota Marosi
CS 1210
Program calculates the distance "as the crow flies" across NYC
"""

import math

def taxicab_distance(streets, avenues):
    taxicab_distance = ((streets/20) + (avenues/7))
    return taxicab_distance

def crow_distance(streets, avenues):
    crow_distance = math.sqrt(((streets/20)**2) + ((avenues/7)**2))
    return crow_distance

how_many_streets = int(input("How many street blocks must you travel? "))
how_many_avenues = int(input("How many avenue blocks must you travel? "))
x = taxicab_distance(how_many_streets, how_many_avenues)
y = crow_distance(how_many_streets, how_many_avenues)
print(f"The crow's flight is {x-y:.2f} miles shorter.")
