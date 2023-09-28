"""
Dakota Marosi
Lab #5, Week 5
September 27th, 2023
CS 1210
"""

def num_to_digits(x):
    digit_one = (x // 100)
    digit_two = (x // 10 % 10)
    digit_three = ((x % 100) % 10)
    final_product = (digit_one, digit_two, digit_three)

    print(final_product)
    return(final_product)

if __name__ == "__main__":
    get_num = int(input("Please give a number on interval 1-999: "))
    digit_list = num_to_digits(get_num)

    max_digit = digit_list[0]
    min_digit = digit_list[2]
    sum_tuple = sum(digit_list)

    print(f"Max digit: {max_digit}, Min digit: {min_digit}, Sum: {sum_tuple}")
