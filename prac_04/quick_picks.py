def main():
    quick_picks = int(input("How many quick picks? "))

    for i in range(quick_picks):
        import random
        numbers = []
        number = range(1, 45)
        numbers.append(number)
        rando = random.choices(number, k=6)
        if number not in numbers:
            numbers.append(number)
        rando.sort()
        print(*rando, sep=' ')


main()