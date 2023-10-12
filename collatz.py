"""
Collatz
Dakota Marosi
CS 1210
Program generates the famous Collatz sequence! :)
"""

def next_collatz(n):
    if n % 2 != 0:
        num = (3 * n + 1)
        return(num)
    else:
        num = (n // 2)
        return(num)

if __name__ == "__main__":
    running = True
    all_nums = []
    
    while running == True:
        get_num = int(input("Enter a positive integer: "))
        if get_num > 0:
            all_nums.append(get_num)
            running = False
        elif get_num <= 0:
            running = True
        
    counter = 0
    while get_num > 1:
        counter += 1
        get_num = next_collatz(get_num)
        all_nums.append(get_num)
    
    print(all_nums)
    print(f"The length of the sequence is {counter + 1}.")
