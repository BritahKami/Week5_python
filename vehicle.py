class Vehicle:

    # Constructor
    def __init__(self, brand, color, yom):

        # Attributes
        self.brand = brand
        self.color = color
        self.yom = yom
    
    def brd(self):
        print(f"The vehicle is of {self.brand} brand")

    def clr(self):
        print(f"The vehicle is of {self.color} color")

    def year(self):
        print(f"The vehicle was made in the year of {self.yom}")
    

carObj = Vehicle("VW", "Red", 2025)
carObj.brd()
carObj.clr()
carObj.year()