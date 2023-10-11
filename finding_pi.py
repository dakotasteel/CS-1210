"""
CS 1210
Lab #7
Dakota Marosi
October 11th, 2023
"""
import random

if __name__ == "__main__":
    num_of_points = int(input("How many numbers of points should we get?: "))

    for n in num_of_points:
        x_coord = (random.random() - 0.5) * 2
        y_coord = (random.random() - 0.5) * 2
