#lex_auth_012748325848399872350
#Start writing your code here
class Instructor:
	def __init__(self):
		self.__instructor_name="Akash"
		self.__experience=4
		self.__avg_feedback=4
		self.__technology_skill=[]
	def set_instructor_name(self,instructor_name):
		self.__instructor_name=instructor_name
	def set_experience(self,experience):
		self.__experience=experience
	def set_avg_feedback(self,avg_feedback):
		self.__avg_feedback=avg_feedback
	def set_technology_skill(self,technology_skill):
		self.__technology_skill=technology_skill
	def get_instructor_name(self):
		print("instructor name: ",self.__instructor_name)
	def get_experience(self):
		print("experience: ",self.__experience)
	def get_avg_feedback(self):
		print("average feedback: ",self.__avg_feedback)
	def get_technology_skill(self):
		print("technology skills: ",self.__technology_skill)
	def check_eligibility(self):
		if self.__experience>3 and self.__avg_feedback>=4.5:
			return 1
		elif self.__experience<=3 and self.__avg_feedback>=4:
			return 1
		else:
			return 0
	def allocate_course(self,technology):
		if self.check_eligibility() and technology in self.__technology_skill:
			return 1
		return 0

instr=Instructor()
instr.set_instructor_name("Akash")
instr.set_experience(4)
instr.set_avg_feedback(4.4)
instr.set_technology_skill(['C','C++','Python'])
print(instr.check_eligibility())
print(instr.allocate_course("Python"))
