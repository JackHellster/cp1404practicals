from taxi import Taxi

taxi = Taxi('Prius 1', 100)
taxi.drive(40)
print(f"{taxi} fare: ${taxi.get_fare():.2f}")

taxi.start_fare()
taxi.drive(100)
print(f"{taxi} fare: ${taxi.get_fare():.2f}")
