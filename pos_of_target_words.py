#lex_auth_0127136518921830401222

def find_target_positions(input_string, target_word):
    target_list=[]
    input_string_list=input_string.split(" ")
    for index in range(len(input_string_list)):
    	if target_word==input_string_list[index]:
    		target_list.append(index)
    return target_list

def find_inverted_index(input_string):
    target_dict={}
    for word in input_string.split(" "):
    	key=word
    	value=find_target_positions(input_string,key)
    	target_dict.update({key:value})
    return target_dict

input_string="we dont need no education we dont need no thought control no we dont"
result_dict=find_inverted_index(input_string)
print(result_dict)
