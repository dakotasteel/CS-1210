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
    for i in lst:
        counter += 1
        mean += i
    mean = mean / counter
    return mean
    
    # Calculate and return the mean of the argument supplied for lst.


def std_dev(lst):
    sum = []
    counter = 0
    average = mean(lst)

    for i in lst:
        new_square = (i - average) ** 2
        sum.append(new_square)
    
    sum_tot = 0
    for i in sum:
        counter += 1
        sum_tot += i
    sum_tot = sum_tot/counter
    sum_tot = math.sqrt(sum_tot)
    return sum_tot

if __name__ == "__main__":
    lst1 = []
    lst2 = []
    with open('co2_ppm.csv', newline = '') as f:
        reader = csv.reader(f)
        for row in reader:
            lst1.append(float(row[0]))
            lst2.append(float(row[1]))

    avg = mean(lst2)
    std_dev_2 = std_dev(lst2)


    # Read data from file into a list of floats
    # Function call(s) to `mean()` and `std_dev()` as needed.
    # Write results to file.
