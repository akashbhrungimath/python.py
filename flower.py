#lex_auth_012727119215337472135
#Start writing your code here
class Flower:
	flower_name_list=['orchid','jasmine','rose']
	order_level=[15,40,25]
	def __init__(self):
		self.__flower_name=None
		self.__price_per_kg=None
		self.__stock_available=None
	def validate_flower(self):
		if self.__flower_name.lower() in Flower.flower_name_list:
			return True
		return False
	def validate_stock(self,required_quantity):
		if required_quantity<=self.__stock_available:
			return True
		return False
	def sell_flower(self,required_quantity):
		if self.validate_flower() and self.validate_stock(required_quantity):
			self.__stock_available-=required_quantity
		else:
			print('Invalid flower name or stock not available')
	def check_level(self):
		for i in range(len(Flower.order_level)):
			if self.__flower_name.lower()==Flower.flower_name_list[i]:
				if self.__stock_available<Flower.order_level[i]:
					return True
				break
		return False
	def set_flower_name(self,flower_name):
		self.__flower_name=flower_name
	def set_price_per_kg(self,price_per_kg):
		self.__price_per_kg=price_per_kg
	def set_stock_available(self,stock_available):
		self.__stock_available=stock_available
	def get_flower_name(self):
		return self.__flower_name
	def get_price_per_kg(self):
		return self.__price_per_kg
	def get_stock_available(self):
		return self.__stock_available

flower1=Flower()
flower1.set_flower_name("Jasmine")
flower1.set_price_per_kg(15)
flower1.set_stock_available(100)
print(flower1.get_stock_available())
flower1.sell_flower(30)
print(flower1.get_stock_available())
print(flower1.check_level())
