"""
CS 1210
Lab #10
Dakota Marosi
November 15th, 2023
"""

if __name__ == "__main__":
    FRIENDS = {"Albert" : ["Victor", "Egbert"],
               "Victor" : ["Albert", "Farrah", "Qani", "Ichabod"],
               "Egbert" : ["Albert", "Farrah", "Qani"],
               "Ichabod": ["Qani", "Farrah", "Victor"],
               "Qani" : ["Ichabod", "Egbert", "Victor"],
               "Farrah" : ["Ichabod", "Egbert", "Victor"],
               "Kamala" : []}

    for keys in FRIENDS:
        print(keys)
    
    for values in FRIENDS.values():
        print(values)

    for keys, values in FRIENDS.items():
        print(f'{keys}: {values}')
