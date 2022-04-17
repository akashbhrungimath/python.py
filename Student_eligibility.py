#lex_auth_012736358230835200606
#Start writing your code here
class Student:
	def __init__(self):
		self.__student_id=234567
		self.__age=20
		self.__marks=97
	def set_student_id(self,student_id):
		self.__student_id=student_id
	def set_age(self,age):
		self.__age=age
	def set_marks(self,marks):
		self.__marks=marks
	def get_student_id(self):
		print("student id : ",self.__student_id)
	def get_age(self):
		print("student age: ",self.__age)
	def get_marks(self):
		print("student marks: ",self.__marks)
	def validate_marks(self):
		if self.__marks>=0 and self.__marks<=100:
			return 1
		return 0
	def validate_age(self):
		if self.__age>20:
			return 1
		return 0
	def check_qualification(self):
		if self.validate_marks() and self.validate_age():
			if self.__marks>=65:
				return 1
		return 0

stu1=Student()
stu1.set_student_id(123456)
stu1.set_age(21)
stu1.set_marks(67)
print(stu1.check_qualification())
