"""
Calorie Tracker
Dakota Marosi
CS 1210
Program mimics calorie tracker
"""

def mean(lst):
    average = sum(lst)/len(lst)
    return average

if __name__ == "__main__":
    calories = []

    print("Welcome to your calorie tracker app!")
    print("Follow the prompts to track your calories throughout the day!")

    bfast = int(input("Enter your calorie count for breakfast: "))
    calories.append(bfast)
    total = sum(calories)
    length = len(calories)
    print(f"You have eaten {total:,} calories from {length} meal")

    mmorn = int(input("Enter your calorie count for mid-morning snack: "))
    calories.append(mmorn)
    total += mmorn
    length += 1
    print(f"You have eaten {total:,} calories from {length} meals")

    lunch = int(input("Enter your calorie count for lunch: "))
    calories.append(lunch)
    total += lunch
    length += 1
    print(f"You have eaten {total:,} calories from {length} meals")

    dinner = int(input("Enter your calorie count for dinner: "))
    calories.append(dinner)
    total += dinner
    length += 1
    print(f"You have eaten {total:,} calories from {length} meals")

    evesnack = int(input("Enter your calorie count for evening snack: "))
    calories.append(evesnack)
    total += evesnack
    length += 1
    print(f"You have eaten {total:,} calories from {length} meals")

    print(f"Total calories consumed: {total:,}")
    average = mean(calories)
    print(f"Average calories per meal/snack: {average:,.1f}")
