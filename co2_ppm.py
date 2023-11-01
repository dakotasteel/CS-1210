"""
Homework 8
Dakota Marosi
CS 1210
"""
import csv

def mean(lst):
    print()
    

def std_dev(lst):
    print()


if __name__ == "__main__":
    with open('co2_ppm.csv', newline = '') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
