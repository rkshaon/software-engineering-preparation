# Encapsulation
Encapsulation is the bundling of data (attributes) and methods (functions) that operate on that data into a single unit or class. It restricts direct access to some of an object's components, which can prevent the accidental modification of data.

## Define class
```
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
```

## Create object
```
my_car = Car("Toyota", "Corolla", 2020)
```

## Access protected attribute through method
```
my_car.drive(100)
print(my_car._mileage)
```