from taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = self.price_per_km * fanciness
        self.flag_fall = 4.50
        self.fanciness = fanciness
        self.current_fare_distance = 0

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flag_fall:.2f}"