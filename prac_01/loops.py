def main():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for i in range(0, 110, 10):
        print(i, end=' ')
    print()

    for i in range(20, 0, -1):
        print(i, end=' ')
    print()

    stars = int(input("Number of stars: "))
    for i in range(0, stars):
        print("*", end='')

    print("\n")

    number = int(input("Number of stars: "))
    for i in range(0, number):
        for j in range(0, i+1):
            print("*", end='')
        print()


main()