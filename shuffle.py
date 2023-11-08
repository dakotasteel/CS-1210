"""
CS 1210
Lab #10
Dakota Marosi
November 8th,, 2023
"""
import random

def shuffle(lst):
    counter = len(lst)
    new_list = []
    for i in range(counter):
        picked_element = random.choice(lst)
        new_list.append(picked_element)
        lst.pop(lst.index(picked_element))
    return(new_list)

if __name__ == "__main__":
    lst = []
    while True:
        list_length = int(input("How many elements in your list? (n > 5): "))
        if list_length > 5:
            break
    
    print(f"Okay. {list_length} items in your list.")
    for i in range(list_length):
        element = (input(f"Enter item at index {i}: "))
        lst.append(element)
    
    old_list = lst.copy()
    new_list = shuffle(old_list)
    print(lst)
    print(new_list)
