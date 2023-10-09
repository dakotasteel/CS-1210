"""
Dakota Marosi
Lab #4, Week 4
CS 1210
"""

get_num = int(input("Enter a positive integer: "))
if get_num <= 0:
    print(f"{get_num} is an invalid input!")
else: 
    print(f"{get_num %1000 %100 %10} is the least significant digit.")
