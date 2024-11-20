from vehicle import Vehicle
from car import Car

if __name__ == "__main__":
    #create an instance of the Vehicle class
    black_car = Vehicle("Tesla", "Model 3", 2018)
    red_car = Vehicle("Toyota", "Camry", 2023)
    real_car = Car("VW", "Bug", 2012, 2)


    all_vehicles = Vehicle.get_all_vehicles()
    for vehicle in all_vehicles:
        print(vehicle)



    