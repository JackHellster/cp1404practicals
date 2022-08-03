"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
def main():

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_to_fahrenheit()
        elif choice == "F":
            fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_celsius():
    """Converts fahrenheit to celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9.0 * (fahrenheit - 32)
    print("Result: {:.2f} C".format(celsius))


def celsius_to_fahrenheit():
    """Converts celsius to fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print ("Result: {:.2f} F".format(fahrenheit))


main()