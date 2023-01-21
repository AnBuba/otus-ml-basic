import exceptions
from abc import ABC
from dataclasses import dataclass


class Vehicle(ABC):
    started = False

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError(f'Low fuel error: fuel = {self.fuel}')

    def move(self):
        if self.fuel >= self.fuel_consumption:
            self.fuel -= self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel(f'Not enough fuel: fuel < fuel consumption')


"""
create dataclass `Engine`
"""


@dataclass
class Engine:
    volume: float = 0
    pistons: str = "Unknown"


"""
создайте класс `Car`, наследник `Vehicle`
"""


class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = []

    def get_engine(self):
        return self.engine

    def set_engine(self, a, b):
        e = Engine(a, b)
        print(e)
        self.engine = [e.volume, e.pistons]


"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):
    cargo = 80

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, value):
        if value + self.cargo <= self.max_cargo:
            self.cargo += value
        else:
            raise exceptions.CargoOverload(f'Cargo overload: {value}')

    def remove_all_cargo(self):
        a = self.cargo
        self.cargo = 0
        print(a)



# test
plane_1 = Plane(907, 75, 15, 100)
print(plane_1.weight, plane_1.fuel, plane_1.fuel_consumption, plane_1.started, plane_1.max_cargo, plane_1.cargo)

plane_1.load_cargo(5)
print(plane_1.weight, plane_1.fuel, plane_1.fuel_consumption, plane_1.started, plane_1.max_cargo, plane_1.cargo)

plane_1.remove_all_cargo()
print(plane_1.weight, plane_1.fuel, plane_1.fuel_consumption, plane_1.started, plane_1.max_cargo, plane_1.cargo)

print()


car_1 = Car(895, 36, 12)
print(car_1.engine)

car_1.set_engine(45, 'privet')
print(car_1.engine)

car_2 = Car(1111, 236, 112)
print(car_2.engine)

car_2.set_engine(99, 'poka')
print(car_2.engine)

vehicle_1 = Vehicle(895, 36, 12)
print(vehicle_1.weight, vehicle_1.fuel, vehicle_1.fuel_consumption, vehicle_1.started)

vehicle_1.start()
print(vehicle_1.weight, vehicle_1.fuel, vehicle_1.fuel_consumption, vehicle_1.started)

vehicle_1.move()
print(vehicle_1.weight, vehicle_1.fuel, vehicle_1.fuel_consumption, vehicle_1.started)


