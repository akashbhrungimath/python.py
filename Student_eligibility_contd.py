#lex_auth_012736365493280768607
#Implement Student class here
class Student:
	def __init__(self):
		self.__student_id=234567
		self.__age=20
		self.__marks=97
		self.__course_id=None
		self.__fees=None
		self.course_ids=[1001,1002]
		self.course_fees=[25575.0,15500.0]
	def set_student_id(self,student_id):
		self.__student_id=student_id
	def set_age(self,age):
		self.__age=age
	def set_marks(self,marks):
		self.__marks=marks
	def set_course_id(self,course_id):
		self.__course_id=course_id
	def set_fees(self,fee):
		self.__fees=fee
	def get_student_id(self):
		print("student id : ",self.__student_id)
	def get_age(self):
		print("student age: ",self.__age)
	def get_marks(self):
		print("student marks: ",self.__marks)
	def get_course_id(self):
		print("student chosen course id : ",self.__course_id)
	def get_fees(self):
		print("fees for the chosen course is : ",self.__fees)
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
	def choose_course(self,course_id):
		if course_id in self.course_ids:
			self.set_course_id(course_id)
			i=self.course_ids.index(course_id)
			if self.__marks>85:
				self.set_fees(self.course_fees[i]-(self.course_fees[i]*25/100))
			else:
				self.set_fees(self.course_fees[i])
			return 1
		return 0

maddy=Student()
maddy.set_student_id(1004)
maddy.set_age(21)
maddy.set_marks(65)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")
