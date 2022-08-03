"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(determine_grade(score))
    import random
    score = (random.randint(0,101))
    print(f'{score} is {determine_grade(score)}')


def determine_grade(score):
    if score > 100 or score < 0:
        return ("Invalid score")
    elif score >= 90:
        return ("Excellent")
    elif score >= 50:
        return("Pass")
    else:
        return ("Bad")

main()




