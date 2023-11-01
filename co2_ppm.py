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
    lst = []
    with open('co2_ppm.csv', newline = '') as f:
        reader = csv.reader(f)
        for row in reader:
            lst.append(float(row[1]))

    avg = mean(lst)
    std_dev_2 = std_dev(lst)
    most_recent = lst[184]

    with open('results.txt', 'w') as f:
        f.write(f'Mean: {avg:.2f}\n')
        f.write(f'Standard deviation: {std_dev_2:.2f}\n')
        f.write(f'Most recent observation: {most_recent:.2f}\n')
