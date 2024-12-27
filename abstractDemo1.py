from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def engine(self):
        pass

class BMWCar(Vehicle):
    def engine(self):
        print("Car Engine")

class BMWBike(Vehicle):
    def engine(self):
        print("Bike Engine")


carobj=BMWCar()
carObj.engine()

bikeObj=BMWBike()
bikeObj.engine()
