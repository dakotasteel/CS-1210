"""
Homework 8
Dakota Marosi
CS 1210
"""
import csv

def mean(lst):
    mean = 0
    counter = 0
    for i in lst:
        counter += 1
        mean +=  lst[i]
    mean = mean / counter
    return mean
    
    # Calculate and return the mean of the argument supplied for lst.


def std_dev(lst):
    print()
    # Calculate and return the standard deviation 
    # of the argument supplied for lst.

if __name__ == "__main__":
    lst1 = []
    lst2 = []
    with open('co2_ppm.csv', newline = '') as f:
        reader = csv.reader(f)
        for row in reader:
            lst1.append(row[1:])
            lst2.append(row[0:1])

    print(lst1)

    # Read data from file into a list of floats
    # Function call(s) to `mean()` and `std_dev()` as needed.
    # Write results to file.
