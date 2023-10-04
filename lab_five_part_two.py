"""
Dakota Marosi
Lab #5, Week 5
September 27th, 2023
CS 1210
"""

if __name__ == "__main__":
    num_one = int(input("Enter the integer for row zero, column zero: "))
    num_two = int(input("Enter the integer for row zero, column one: "))
    num_three = int(input("Enter the integer for row one, column zero: "))
    num_four = int(input("Enter the integer for row one, column one: "))
    number_list = [[num_one, num_two],[num_three, num_four]]

    print(f" The 2x2 list is: {number_list}")
