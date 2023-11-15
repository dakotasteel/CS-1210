"""
Homework 10
November 14th
Dakota Marosi
CS 1210
"""

if __name__ == '__main__':
    while True:
        try:
            get_name = input("Enter name of file you want to open:")
            file = open(get_name, "r")
            counter = 0
            for line in file:
                counter += 1
                print(line)
            if counter > 0:
                break

        except FileNotFoundError:
            if get_name == "q":
                break
            print(f'"{get_name}" cannot be found in this directory. Please enter a new file name.')
            
