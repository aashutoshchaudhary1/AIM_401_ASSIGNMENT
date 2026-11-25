"""LogiTrans Logistics - Fleet Management Prototype (Lesson 5)
Demonstrates abstraction, encapsulation, inheritance and polymorphism."""

from abc import ABC, abstractmethod


# ---------- Task 1 and 2: abstract base class with protected rate ----------
class Vehicle(ABC):
    def __init__(self, vehicle_id, model, daily_rate):
        self.vehicle_id = vehicle_id
        self.model = model
        self.set_daily_rate(daily_rate)      # validated through the setter

    def get_daily_rate(self):
        return self.__daily_rate

    def set_daily_rate(self, rate):
        if rate <= 0.0:
            raise ValueError("Daily rate must be greater than 0.0")
        self.__daily_rate = rate

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass

    def __lt__(self, other):                 # lets sorted() compare vehicles
        return self.get_daily_rate() < other.get_daily_rate()


# ---------- Task 3 and 4: child classes ----------
class PassengerCar(Vehicle):
    def __init__(self, vehicle_id, model, daily_rate, num_seats):
        super().__init__(vehicle_id, model, daily_rate)
        self.num_seats = num_seats

    def calculate_rental_cost(self, days):
        return (self.get_daily_rate() * days) + (15.0 * self.num_seats)

    def __str__(self):
        return (f"PassengerCar [{self.vehicle_id}] {self.model} | "
                f"Seats: {self.num_seats} | Rate: ${self.get_daily_rate():.2f}/day")


class CargoTruck(Vehicle):
    def __init__(self, vehicle_id, model, daily_rate, cargo_capacity_tons):
        super().__init__(vehicle_id, model, daily_rate)
        self.cargo_capacity_tons = cargo_capacity_tons

    def calculate_rental_cost(self, days):
        return (self.get_daily_rate() * days) + (50.0 * self.cargo_capacity_tons)

    def __str__(self):
        return (f"CargoTruck [{self.vehicle_id}] {self.model} | "
                f"Capacity: {self.cargo_capacity_tons} tons | Rate: ${self.get_daily_rate():.2f}/day")


# ---------- Polymorphic processing (no isinstance / type checks) ----------
def generate_fleet_manifest(fleet_list, days):
    print(f"FLEET MANIFEST - {days}-day rental")
    print("-" * 70)
    total = 0
    for vehicle in fleet_list:
        cost = vehicle.calculate_rental_cost(days)
        print(vehicle)
        print(f"    Cost for {days} days: ${cost:.2f}")
        total += cost
    print("-" * 70)
    print(f"Grand total: ${total:.2f}")
    return total


# ---------- Demonstration ----------
if __name__ == "__main__":
    print("TEST 1: abstract class")
    try:
        Vehicle("V000", "Generic", 50.0)
    except TypeError as error:
        print("TypeError:", error)

    print("\nTEST 2: rate validation")
    car = PassengerCar("PC001", "Toyota Corolla", 45.0, 5)
    print("Rate:", car.get_daily_rate())
    for bad_rate in (0, -20.0):
        try:
            car.set_daily_rate(bad_rate)
        except ValueError as error:
            print(f"Rejected {bad_rate}: {error}")
    print("Rate is still:", car.get_daily_rate())

    fleet = [
        PassengerCar("PC001", "Toyota Corolla", 45.0, 5),
        PassengerCar("PC002", "Hyundai Creta", 60.0, 7),
        CargoTruck("CT001", "Tata Prima", 120.0, 10.0),
        CargoTruck("CT002", "Ashok Leyland Boss", 95.0, 6.5),
    ]

    print("\nTEST 3: manifest")
    generate_fleet_manifest(fleet, 3)

    print("\nTEST 4: sorted by daily rate")
    for vehicle in sorted(fleet):
        print(vehicle)
