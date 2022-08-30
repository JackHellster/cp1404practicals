from guitar import Guitar

def main():
    guitars = []
    print("My guitars!")
    while True:
        name = input("Name: ")
        if name != '':
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
            print(guitar, "added.\n")
        else:
            break
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    display_guitar_list(guitars)


def display_guitar_list(guitar_list):
    i = 0
    print()
    print("... snip ...")
    print()
    print("These are my guitars:")
    for guitar in guitar_list:
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i+1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
        i = i+1


main()