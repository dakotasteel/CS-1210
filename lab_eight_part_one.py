"""
CS 1210
Lab #8
Dakota Marosi
October 25th, 2023
"""
import csv

if __name__ == "__main__":
    a_team = 0
    b_team = 0

    with open('doc.csv', 'r') as my_doc:
        reader = csv.reader(my_doc)
        for row in reader:
            name, team, score = row
            if team == "A":
                a_team += float(score)
            else:
                b_team += float(score)
    print(f"The A team's score is {a_team:.2f}, and the B team's score is {b_team:.2f}.")
