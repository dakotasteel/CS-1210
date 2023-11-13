"""
CS 1210
In Class Exercise
Dakota Marosi
November 6th, 2023
Raising Errors!
"""
import math

if __name__ == "__main__":
    #TypeError
    lst = [1, 2, 3]
    print(f'{lst - 1}')

    #SyntaxError
    if True
        print("True")
    
    #IndentationError
    if True:
    print("True")

    #NameError
    y = x + 1

    #AttributeError
    z = math.pie

    #ZeroDivisionError
    zero_div = 8 / 0

    #IndexError
    lst2 = ['apple', 'orange', 'lime', 'lemon']
    lst2[5]

    #FileNotFoundError
    open('file that does not exist')
