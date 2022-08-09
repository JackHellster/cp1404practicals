from statistics import mean
def main():

    numbers = []
    total_number = int(input("How many numbers? \n"))

    for i in range(total_number):
        number = float(input("Number: "))
        numbers.append(number)
    find_first_number(numbers)
    find_last_number(numbers)
    find_smallest_number(numbers)
    find_largest_number(numbers)
    find_average(numbers)

    security_check()


def security_check():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user = input("Enter username: ")
    while user not in usernames:
        print("Access denied")
        user = input("Enter username: ")
    else:
        print("Access granted")


def find_last_number(numbers):
    print(f"The last number is {numbers[-1]:.0f}")


def find_first_number(numbers):
    print(f"The first number is {numbers[0]:.0f}")

def find_smallest_number(numbers):
    print(f"The smallest number is {min(numbers):.0f}")


def find_largest_number(numbers):
    print(f"The largest number is {max(numbers):.0f}")


def find_average(numbers):
    print(f"The average of the numbers is {mean(numbers)}")





main()

