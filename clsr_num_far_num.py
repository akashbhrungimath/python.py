#lex_auth_0127136008767324161169

def close_number(num1,num2,num3):
    num_list=[num1,num2,num3]
    flag=False
    for index1 in range(len(num_list)):
    	for index2 in range(index1+1,len(num_list)):
    		if num_list[index1]+1==num_list[index2] or num_list[index1]==num_list[index2]+1 or num_list[index1]==num_list[index2]:
    			index_of_clsr_num1=index1
    			index_of_clsr_num2=index2
    			flag=True
    			break
    	if(flag):
    		break
    
    if(flag):
    	for index in range(len(num_list)):
    		if index!=index_of_clsr_num1 and index!=index_of_clsr_num2:
    			if abs(num_list[index] - num_list[index_of_clsr_num1])>=2 and abs(num_list[index] - num_list[index_of_clsr_num2])>=2:
    				 return True
    return False

print(close_number(6,9,6))
