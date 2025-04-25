from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, color, yom, speed):
        super().__init__(brand, color, yom)

        self.speed = speed

    def brd(self):
        print(f"I am driving a {self.brand}")

    def spd(self):
        print(f"My car's top speed is {self.speed}")

car = Car("Toyota", "Green", 1990, 200)

car.brd()