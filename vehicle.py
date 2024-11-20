# Parent Class
class Vehicle:

    wheels = 4 #Class level attribute assigned to all objects from the class


    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year