#lex_auth_012751124968554496166
#Start writing your code here
class Classroom:
	classroom_list=['L12','G345','L123']
	@staticmethod
	def search_classroom(class_room):
		for classroom in Classroom.classroom_list:
			if (classroom[0].lower()=='l' and class_room==int(classroom[1:])) or class_room.lower()==classroom.lower():
				return "Found"
		return -1

print(Classroom.search_classroom(123))
