#lex_auth_012748317267525632347
#Start writing your code here
class Ticket:
	counter=1
	destination_list=["mumbai","chennai","kolkata","pune"]
	def __init__(self,passenger_name,source,destination):
		self.__passenger_name=passenger_name
		self.__ticket_id=""
		self.__source=source
		self.__destination=destination
	def validate_source_destination(self):
		if self.__source.lower()=="delhi" and self.__destination.lower() in Ticket.destination_list:
			return True
		return False
	def generate_ticket(self):
		if self.validate_source_destination():
			self.__ticket_id+="D"
			if self.__destination.lower()==Ticket.destination_list[0]:
				self.__ticket_id+="M"
			elif self.__destination.lower()==Ticket.destination_list[1]:
				self.__ticket_id+="C"
			elif self.__destination.lower()==Ticket.destination_list[2]:
				self.__ticket_id+="K"
			elif self.__destination.lower()==Ticket.destination_list[3]:
				self.__ticket_id+="P"
			else:
				print("Invalid destination")
			if Ticket.counter<10:
				self.__ticket_id+="0"
				self.__ticket_id+=str(Ticket.counter)
			else:
				self.__ticket_id+=str(Ticket.counter)
			Ticket.counter+=1
		else:
			self.__ticket_id=None
	def get_ticket_id(self):
		return self.__ticket_id
	def get_passenger_name(self):
		return self.__passenger_name
	def get_source(self):
		return self.__source
	def get_destination(self):
		return self.__destination

passenger1=Ticket("Akash","Delhi","Mumbai")
passenger1.generate_ticket()
print(passenger1.get_ticket_id())
