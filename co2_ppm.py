"""
Homework 8
Dakota Marosi
CS 1210
"""
import csv
import math

def mean(lst):
    mean = 0
    counter = 0
    for _ in range(185):
        counter += 1
        mean +=  int(lst[_:])
    mean = mean / counter
    return mean
    
    # Calculate and return the mean of the argument supplied for lst.


def std_dev(lst):
    sum = []
    average = 0

    for _ in range(5):
        average +=  lst[_]
    average = average / 5

    for _ in range(5):
        new_square = (lst[_] - average) ** 2
        sum.append(new_square)
    
    sum_tot = 0
    for _ in range(5):
        sum_tot += sum[_]
    sum_tot = sum_tot/5
    sum_tot = math.sqrt(sum_tot)
    return sum_tot

if __name__ == "__main__":
    lst1 = []
    lst2 = []
    with open('co2_ppm.csv', newline = '') as f:
        reader = csv.reader(f)
        for row in reader:
            lst1.append(row[1:])
            lst2.append(row[0:1])

    mean(lst1)

    # Read data from file into a list of floats
    # Function call(s) to `mean()` and `std_dev()` as needed.
    # Write results to file.
