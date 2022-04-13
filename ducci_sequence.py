#lex_auth_0127136216235950081185

def ducci_sequence(test_list,n):
    final_list=[]
    for index in range(n+1):
    	ducci_list=[]
    	for index1 in range(len(test_list)):
    		if index1==len(test_list)-1:
    			ducci_list.append(abs(test_list[index1]-test_list[0]))
    		else:
    			ducci_list.append(abs(test_list[index1]-test_list[index1+1]))
    	final_list.append(ducci_list)
    	test_list=ducci_list
    return final_list[n]

ducci_element=ducci_sequence([7, 60, 861, 3070] , 3)
print(ducci_element)
