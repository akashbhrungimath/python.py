#lex_auth_012753080343093248327
#Start writing your code here
class FruitInfo:
	__fruit_name_list=['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
	__fruit_price_list=[100, 800, 70, 110, 600]
	@staticmethod
	def get_fruit_price(fruit_name):
		if fruit_name in FruitInfo.__fruit_name_list:
			for index in range(len(FruitInfo.__fruit_name_list)):
				if FruitInfo.__fruit_name_list[index]==fruit_name:
					return FruitInfo.__fruit_price_list[index]
		else:
			return -1
	@staticmethod
	def get_fruit_name_list():
		return FruitInfo.__fruit_name_list
	@staticmethod
	def get_fruit_price_list():
		return FruitInfo.__fruit_price_list

class Customer:
	def __init__(self,customer_name,cust_type):
		self.__customer_name=customer_name
		self.__cust_type=cust_type
	def get_customer_name(self):
		return self.__customer_name
	def get_cust_type(self):
		return self.__cust_type

class Purchase:
	__counter=101
	def __init__(self,customer,fruit_name,quantity):
		self.__purchase_id=None
		self.__customer=customer
		self.__fruit_name=fruit_name
		self.__quantity=quantity
	def get_purchase_id(self):
		return self.__purchase_id
	def get_customer(self):
		return self.__customer
	def get_quantity(self):
		return self.__quantity
	def calculate_price(self):
		price_per_fruit=FruitInfo.get_fruit_price(self.__fruit_name)
		price=price_per_fruit
		if price!=-1:
			price=price_per_fruit*self.__quantity
			flag=False
			price_list=FruitInfo.get_fruit_price_list()
			if self.__quantity>1:
				flag=True
				for index in range(len(price_list)):
					if price_per_fruit<price_list[index]:
						flag=False
						break
			if flag:
				price-=price*0.02
			elif self.__quantity>=5:
				flag=True
				for index in range(len(price_list)):
					if price_per_fruit>price_list[index]:
						flag=False
						break
				if flag:
					price-=price*0.05
			customer_type=self.__customer.get_cust_type()
			if customer_type.lower()=="wholesale":
				price-=price*0.1
			self.__purchase_id="P"+str(Purchase.__counter)
			Purchase.__counter+=1
			return price
		else:
			return -1

cust1=Customer("Akash","wholesale")
pur1=Purchase(cust1,"Orange",5)
print(pur1.calculate_price())
print(pur1.get_purchase_id())
