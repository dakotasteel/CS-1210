"""
Dakota Marosi
Lab #4, Week 4
CS 1210
"""

get_num = int(input("Enter any integer: "))
if get_num >= -9 and get_num <= 9:
    print(f"{get_num} doesn't have enough digits!")
else: 
    print(f"{get_num //10 %10} is the least significant digit.") 
    # this only works for integers between 10 and 999, anything 1000 above
    # would result in an incorrect answer
