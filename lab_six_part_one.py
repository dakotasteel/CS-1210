"""
Bee and Dakota
CS 1210
Lab 6
"""
#currently broken :D i never did figure it out.
def min(lst):
    for i in lst:
        counter = 0
        x = 0
        y = 0
        min = 0
        while counter == True:
            x = lst[counter]
            print(x)
            y = lst[counter+1]
            print(y)
            if x > y:
                min = y
                print(y)

if __name__ == "__main__":
    min([1, 2, 3])

