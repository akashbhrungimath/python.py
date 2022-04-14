#lex_auth_01275044879016755225
#Start writing your code here
class Vehicle:
    def __init__(self,mileage,fuel_left):
        self.mileage=mileage
        self.fuel_left=fuel_left
    def identify_distance_that_can_be_travelled(self):
        if self.fuel_left>5:
            return self.mileage*(self.fuel_left-5)
        else:
            return 0
    def identify_distance_travelled(self,initial_fuel):
        return (initial_fuel-self.fuel_left)*self.mileage

mileage=12
fuel_left=6
initial_fuel=25
Car=Vehicle(mileage,fuel_left)
print(Car.identify_distance_that_can_be_travelled())
print(Car.identify_distance_travelled(initial_fuel))
