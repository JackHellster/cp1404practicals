NAME_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff", "amaranth": "#e52b50",
                "amber": "#ffbf00", "apricot": "#fbceb1", "aqua": "#00ffff"}
print(NAME_TO_CODE)

colour_code = input("Enter short state: ").lower()
while colour_code != "":
    if colour_code in NAME_TO_CODE:
        print(f"{colour_code:3} is {NAME_TO_CODE[colour_code]}")
    else:
        print("Invalid short state")
    colour_code = input("Enter short state: ").lower()