#lex_auth_012727139457941504148
#Start writing your code here       
class Bill:
	def __init__(self,bill_id,patient_name):
		self.__bill_id=bill_id
		self.__patient_name=patient_name
		self.__bill_amount=None
	def calculate_bill_amount(self,consultation_fees,quantity_list,price_list):
		self.__bill_amount=consultation_fees
		for i in range(len(quantity_list)):
			self.__bill_amount+=quantity_list[i]*price_list[i]
	def get_bill_id(self):
		return self.__bill_id
	def get_patient_name(self):
		return self.__patient_name
	def get_bill_amount(self):
		return self.__bill_amount

pat1=Bill(1234,"xyz")
pat1.calculate_bill_amount(1000,[2,1,3],[10,5,2])
print(pat1.get_bill_id())
print(pat1.get_patient_name())
print(pat1.get_bill_amount())
