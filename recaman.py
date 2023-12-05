"""
Dakota Marosi
CS1210
Homework 12 (Extra Credit)
"""

def next_recaman(lst):
    if len(lst) == 0:
        lst.append(0)
        return lst
    elif (lst[-1] - len(lst)) > 0 and (lst[-1] - len(lst)) not in lst:
        lst.append(lst[-1] - len(lst))
        return lst
    else:
        lst.append(lst[-1] + len(lst))
        return lst

