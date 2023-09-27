"""
Tree Identifier
Dakota Marosi
CS 1210
Program identifies a tree given user input option and using 
conditionals
"""

leaves_or_needles = input("Does it have leaves (l) or needles (n)? ")
leaves_or_needles = leaves_or_needles.lower()

if leaves_or_needles == "l":
    simple_or_compound = input("Are the leaves simple (s) or compound (c)? ")
    simple_or_compound = simple_or_compound.lower()
    if simple_or_compound == "s":
        print("Maple")
    elif simple_or_compound == "c":
        print("Ash")
    else:
        print("Invalid choice!")
elif leaves_or_needles == "n":
    individ_or_clust = input("Are needles individual or clustered (i or c)? ")
    individ_or_clust = individ_or_clust.lower()
    if individ_or_clust == "i":
        print("Spruce")
    elif individ_or_clust == "c":
        print("Pine")
    else:
        print("Invalid choice!")
else:
    print("Invalid choice!")


