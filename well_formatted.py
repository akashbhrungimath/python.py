#lex_auth_0127136426924195841210

def check_well_formatted(input_item,list_label):
    flag=True
    if type(input_item)== list and len(input_item)>=2 and input_item[0] in list_label:
    	for index in range(1,len(input_item)):
    		if not(type(input_item[index])== list or type(input_item[index])== str):
    			flag=False
    			break
    else:
    	flag=False
    if flag==True:
    	for index in range(1,len(input_item)):
    		if type(input_item[index])== list:
    			flag=check_well_formatted(input_item[index],list_label)
    return flag

input_list1=['Apple']
list_label1=['Apple']
result=check_well_formatted(input_list1,list_label1)
if result is True:
    print("Well formatted")
else:
    print("Not Well formatted")
