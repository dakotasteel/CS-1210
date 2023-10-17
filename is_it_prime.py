"""
Is It Prime?
Dakota Marosi
CS 1210
Program tests if a user inputted number is prime or not
"""


def prime_test(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    else:
        return True


if __name__ == "__main__":
    running = True
    while running == True:
        get_num = int(input("Enter an integer > 1: "))
        if get_num <= 1:
            running = True
        else:
            running = False

    t_or_f = prime_test(get_num)

    if t_or_f == False:
        print(f"{get_num} is not prime.")
    else:
        print(f"{get_num} is prime.")
