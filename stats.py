"""
Euclidean Division
Dakota Marosi
CS 1210
Program calculates average and standard deviation 
of user inputted numbers
"""

def mean(lst):
    mean = 0
    for _ in range(5):
        mean +=  lst[_]
    mean = mean / 5
    return mean

def std_dev(lst):
    sum = []
    mean = 0
    
    for _ in range(5):
        mean +=  lst[_]
    mean = mean / 5

    for _ in range(5):
        new_square = (lst[_] - mean) ** 2
        sum.append(new_square)
    
    sum_tot = 0
    for _ in range(5):
        sum_tot += sum[_]
        print(sum_tot)
    sum_tot = sum_tot/5
    print(sum_tot)
    return sum_tot

if __name__ == "__main__":
    numbers = []
    for _ in range(5):
        new_num = float(input("Enter a real number: "))
        numbers.append(new_num)

    avg = mean(numbers)
    dev = std_dev(numbers)
    print(f"The mean is {avg:.3f} and the standard deviation is {dev:.3f}")
