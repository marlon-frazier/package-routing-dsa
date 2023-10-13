#Truck class / definition
class Truck:
    def __init__(self, capacity, speed, load, packages, mileage, address, depart_time):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time

    def __str__(self):
        return f"Capacity: {self.capacity}, Speed: {self.speed}, Load: {self.load}, Packages: {self.packages}, Mileage: {self.mileage}, Address: {self.address}, Departure Time: {self.depart_time}"
