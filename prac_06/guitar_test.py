from guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

another_name = "Another Guitar"
another_year = 2013
another_cost = 589

guitar = Guitar(name, year, cost)
another = Guitar(another_name, another_year, another_cost)

print(f"{name} get_age() - Expected {guitar.get_age()}. Got {guitar.get_age()}")
print(f"{another_name} get_age() - Expected {another.get_age()}. Got {another.get_age()}")
print(f"{name} is_vintage() - Expected {guitar.is_vintage()}. Got {guitar.is_vintage()}")
print(f"{another_name} is_vintage() - Expected {another.is_vintage()}. Got {another.is_vintage()}")