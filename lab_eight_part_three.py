"""
CS 1210
Lab #8
Dakota Marosi
October 25th, 2023
"""
if __name__ == "__main__":
    counter = 0
    file_name = input("Give a file name you want to read: ")
    with open(file_name, 'r') as f:
        for line in f:
            counter += 1
            print(f'{counter}: {line}')
