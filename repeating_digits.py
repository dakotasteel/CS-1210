"""
Dakota Marosi
Lab #4, Week 4
CS 1210
"""

get_num = int(input("Please give an integer in the range 1-9: "))
if get_num <= 0 and get_num >= 9:
    print(f"{get_num} is an invalid input!")
else:
    print(f"{get_num *123} is the result.")
