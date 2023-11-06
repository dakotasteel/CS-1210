"""
CS 1210
Lab #8
Dakota Marosi
October 25th, 2023
"""
import csv

if __name__ == "__main__":
    counter = 0
    with open('part_two.py', 'r') as f:
        for line in f:
            counter += 1
            string = f'{counter:>4}: {line}'
            stripped = string.strip('\n')
            print(stripped)
