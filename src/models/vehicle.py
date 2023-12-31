from src.enums.enums import VehicleType


class Vehicle:
    def __init__(self, plate_number, vehicle_type):
        self.plate_number = plate_number
        self.vehicle_type = vehicle_type

    def get_details(self):
        return f"Plate Number: {self.plate_number}, Vehicle Type: {self.vehicle_type}"


class Car(Vehicle):
    def __init__(self, plate_number):
        super().__init__(plate_number, VehicleType.CAR)


class Truck(Vehicle):
    def __init__(self, plate_number):
        super().__init__(plate_number, VehicleType.TRUCK)


class Van(Vehicle):
    def __init__(self, plate_number):
        super().__init__(plate_number, VehicleType.VAN)


class MotorBike(Vehicle):
    def __init__(self, plate_number):
        super().__init__(plate_number, VehicleType.MOTORBIKE)


class ElectricVehicle(Vehicle):
    def __init__(self, plate_number):
        super().__init__(plate_number, VehicleType.ELECTRIC)
