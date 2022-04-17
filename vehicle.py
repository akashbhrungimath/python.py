#lex_auth_012736349701922816604
#Start writing your code here
class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None
    
    def set_vehicle_id(self,vehicle_id):
    	self.__vehicle_id=vehicle_id
    
    def set_vehicle_cost(self,vehicle_cost):
    	self.__vehicle_cost=vehicle_cost
    
    def set_vehicle_type(self,vehicle_type):
    	self.__vehicle_type=vehicle_type
    
    def get_vehicle_id(self):
    	print("vehicle_id: ",self.__vehicle_id)
    
    def get_vehicle_cost(self):
    	print("vehicle_cost: ",self.__vehicle_cost)
    
    def get_vehicle_type(self):
    	print("vehicle_type: ",self.__vehicle_type)
    
    def set_premium_amount(self,premium_amount):
    	self.__premium_amount=premium_amount
    
    def get_premium_amount(self):
    	print("premium_amount: ",self.__premium_amount)
    
    def calculate_premium(self):
    	if self.__vehicle_type=="TwoWheeler":
    		self.__premium_amount=2*self.__vehicle_cost/100
    	elif self.__vehicle_type=="FourWheeler":
    		self.__premium_amount=6*self.__vehicle_cost/100
    	else:
    		self.__premium_amount=None
    		print("Invalid vehicle type")
    
    def display_vehicle_details(self):
    	print("premium_amount: ",self.__premium_amount)

vehicle_type="TwoWheeler"
vehicle_cost=105000
car=Vehicle()
car.set_vehicle_cost(105000)
car.set_vehicle_type("TwoWheeler")
car.calculate_premium()
car.display_vehicle_details()
