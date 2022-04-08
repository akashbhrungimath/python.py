#lex_auth_0127136332814499841204

def sum_of_elements(num_list,number):
    while (number in num_list):
    	pos_index=num_list.index(number)
    	for index in range(3):
    		if(pos_index>0 and pos_index<=len(num_list)):
    			num_list.pop(pos_index-1)
    		else:
    			pos_index+=1
    result_sum=0
    for num in num_list:
    	result_sum+=num
    return result_sum

num_list=[2,3,4,5,6,2,3]
number=2
print(sum_of_elements(num_list, number))
