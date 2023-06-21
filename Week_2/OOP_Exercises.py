# Exercise 1
class Vehicle:
    def __init__(self, max_speed: int, mileage: int):
        self.max_speed = max_speed
        self.mileage = mileage


RAV4 = Vehicle(90, 18)
print(RAV4.max_speed, RAV4.mileage)


# Exercise 2
class Vehicle:
    pass


# Exercise 3
class Vehicle:
    def __init__(self, name, max_speed: int, mileage: int):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


# only inherit variables & methods
class Bus(Vehicle):
    pass


Sbus = Bus("Volvo Double-decker", 90, 18)
print("Name:", Sbus.name, "Speed:", Sbus.max_speed, "Mileage:", Sbus.mileage)


# Exercise 4
# class inheritance
class Vehicle:
    def __init__(self, name, max_speed: int, mileage: int):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


Sbus = Bus("Volvo double-decker", 90, 18)
print(Sbus.seating_capacity())


# Exercise 5
class Vehicle:
    # class attribute
    color = "White"

    def __init__(self, name, max_speed: int, mileage: int):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


Sbus = Bus("Volvo Double-decker", 90, 18)
print(Sbus.color, Sbus.name, "Speed:", Sbus.max_speed, "Mileage:", Sbus.mileage)

car = Car("RAV4 LE", 200, 23)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)


# Exercise 6
# super() to access parent class
class Vehicle:
    def __init__(self, name, max_speed: int, capacity: int):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount


Sbus = Bus("Volvo Double-decker", 90, 18)
print("The total bus fare is:", Sbus.fare())


# Exercise 7
class Vehicle:
    def __init__(self, name, max_speed: int, capacity: int):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity


class Bus(Vehicle):
    pass


Sbus = Bus("Volvo Double-decker", 90, 18)

# built in to find class of given bus type()
print(type(Sbus))


# Exercise 8
# built in isinstance() to find if Sbus is an instance of vehicle class
class Vehicle:
    def __init__(self, name, max_speed: int, capacity: int):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity


class Bus(Vehicle):
    pass


Sbus = Bus("Volvo Double-decker", 90, 18)
# need the bus and the class to pull from
print(isinstance(Sbus, Vehicle))