from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
fare = 0
chosen_taxi = None
number = [0,1,2]

def menu():
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").lower()

    if choice == "q":
        return False
    elif choice == "c":
        i = 0
        print("Taxis available:")
        for car in taxis:
            print(f"{i} - {car}")
            i += 1
        try:
            car_number = int(input("Choose taxi: "))
            global chosen_taxi
            chosen_taxi = car_number
            taxis[car_number]
            return True
        except IndexError:
            print("Invalid taxi choice")
            return True
        except ValueError:
            print("Invalid taxi choice")
            return True

    elif choice == "d":
        drive(chosen_taxi)
        return True
    else:
        print("Invalid option")
        return True

def drive(car_number):
    if car_number is None:
        print("You need to choose a taxi before you can drive")

    else:
        distance = int(input("Drive how far? "))
        chosen = taxis[car_number]
        chosen.drive(distance)
        global fare
        try:
            fare = fare + chosen.get_fare() + chosen.flagfall
            print(f"Your {chosen.name} trip cost you ${chosen.get_fare():.2f}")

        except AttributeError:
            fare = fare + chosen.get_fare()
            print(f"Your {chosen.name} trip cost you ${chosen.get_fare():.2f}")



def main():
    print("Let's drive!")
    while menu() is True:
        print(f"Bill to date: ${fare:.2f}")
    print(f"Total trip cost: ${fare:.2f}")
    print("Taxis are now:")
    i = 0
    for car in taxis:
        print(f"{i} - {car}")
        i += 1





main()