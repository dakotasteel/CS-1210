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
        new_list = new_list.append(picked_element)
        lst.pop(lst.index(picked_element))
    print()

if __name__ == "__main__":
    old_list = []
    list_length = 0
    while list_length == 0:
        list_length = int(input("How many elements in your list? (n > 5): "))
    
    print(f"Okay. {list_length} items in your list.")
    for i in range(list_length):
        element = int(input(f"Enter item at index {i}: "))
        old_list.append(element)

    new_list = shuffle(old_list)
    print(old_list)
    print(new_list)

        
