"""
Euclidean Division
Dakota Marosi
CS 1210
Program does Euclidean divison by 
repeated subtraction & modulus, a la the old days
"""
def quotient(r, s):
    print("This is quotient")
    counter = 0
    while r >= s:
        r = r - s
        counter += 1
    return counter

def remainder(r, s):
    counter = 0
    while r >= s:
        r = r - s
        counter += 1
    return r

if __name__ == "__main__":
    running = True
    while running == True:
        get_dividend = int(input("Enter the dividend (positive integer): "))
        if get_dividend <= 0:
            running = True
        else:
            running = False

    running = True
    while running == True:
        get_divisor  = int(input("Enter the divisor (positive integer): "))
        if get_divisor <= 0:
            running = True
        else:
            running = False

    quot_ans = quotient(get_dividend, get_divisor)
    rem_ans = remainder(get_dividend, get_divisor)
    

    print(f"{get_dividend} // {get_divisor} = {quot_ans}")
    print(f"{get_dividend} % {get_divisor} = {rem_ans}")
