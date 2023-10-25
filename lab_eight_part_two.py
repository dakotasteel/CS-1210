"""
CS 1210
Lab #8
Dakota Marosi
October 25th, 2023
"""
if __name__ == "__main__":
    counter = 0
    with open('part_two.py', 'r') as f:
        for line in f:
            counter += 1
            print(f'{counter}: {line}')
