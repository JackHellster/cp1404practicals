number = int(input("Number of items: "))
total = []
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(0, number):
    price = float(input("Price of item: "))
    total.append(price)

if sum(total) > 100:
    print(f"Total price for {number} items is ${sum(total)*0.9:.2f}")
else:
    print(f"Total price for {number} items is ${sum(total):.2f}")


