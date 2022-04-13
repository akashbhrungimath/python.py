def list_rotate(uniquecode_list):
    rotated_list=[]
    for unique_code in uniquecode_list:
    	code_list=unique_code.split("-")
    	count=0
    	rotated_code=""
    	for char in code_list[0]:
    		if char.isalpha():
    			rotated_code+=char
    			count+=1
    	for index in range(count):
    		temp=code_list[1][-1]
    		code_list[1]=code_list[1][:3]
    		code_list[1]=temp+code_list[1]
    	rotated_code+=code_list[1]
    	rotated_list.append(rotated_code)
    return rotated_list

#You may modify the below code for testing
uniquecode_list=["AZ01-1234","R137-8714"]
rotated_list = list_rotate(uniquecode_list)
print(rotated_list)
