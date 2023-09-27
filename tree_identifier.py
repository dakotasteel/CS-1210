"""
Tree Identifier
Dakota Marosi
CS 1210
Program identifies a tree given user input option and using 
conditionals
"""
if __name__ == '__main__':

    leaves_or_needles = input("Does it have leaves (l) or needles (n)? ")
    leaves_or_needles = leaves_or_needles.lower()

    if leaves_or_needles == "l":
        simple_or_compound = input("Are leaves simple (s) or compound (c)? ")
        simple_or_compound = simple_or_compound.lower()
        if simple_or_compound == "s":
            print("Maple")
        elif simple_or_compound == "c":
            print("Ash")
        else:
            print("Invalid choice!")
    elif leaves_or_needles == "n":
        needle_type = input("Are needles individual or clustered (i or c)? ")
        needle_type = needle_type.lower()
        if needle_type == "i":
            print("Spruce")
        elif needle_type == "c":
            print("Pine")
        else:
            print("Invalid choice!")
    else:
        print("Invalid choice!")
