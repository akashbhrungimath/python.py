#lex_auth_0127136373866577921209

def integer_to_english(number):
    if number==0:
    	return "zero"
    if not(number>=0 and number<=1000):
    	return -1
    unit_digit_list=["one","two","three","four","five","six","seven","eight","nine"]
    teen_num_list=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    multiples_of_ten_list=["ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninty"]
    temp=number
    num_list=[]
    while(temp!=0):
    	remainder=temp%10
    	num_list.append(remainder)
    	temp//=10
    num_words=""
    for index in range(len(num_list),0,-1):
    	if index==4:
    		if num_list[index-1]==0:
    			continue
    		num_words+=unit_digit_list[num_list[index-1]-1]
    		num_words+=" thousand"
    	elif index==3:
    		if num_list[index-1]==0:
    			continue
    		if len(num_words):
    			num_words+=" "
    		num_words+=unit_digit_list[num_list[index-1]-1]
    		num_words+=" hundred"
    	elif index==2:
    		if num_list[index-1]==0:
    			continue
    		if len(num_words):
    			num_words+=" and "
    		if num_list[index-1]==1 and num_list[index-2]!=0:
    			num_words+=teen_num_list[num_list[index-2]-1]
    			break
    		elif num_list[index-1]!=1:
    			num_words+=multiples_of_ten_list[num_list[index-1]-1]
    			num_words+=" "
    		else:
    			num_words+=multiples_of_ten_list[0]
    			break
    	elif index==1:
    		if num_list[index-1]==0:
    			continue
    		if ((not num_words.count(" and ")) and len(num_words)):
    			num_words+=" and "
    		num_words+=unit_digit_list[num_list[index-1]-1]
    return num_words

number=12
print(integer_to_english(number))
