

class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self._mileage = 0 # Protected attribute

    def drive(self, miles):
        if miles > 0:
            self._mileage += miles # Modification of protected attribute
        
    def get_mileage(self):
        return self._mileage



my_car = Car("Toyota", "Corolla", 2020)

my_car.drive(100)
print(my_car._mileage)