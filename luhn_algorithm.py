#lex_auth_01269445968039936095

def validate_credit_card_number(card_number):
    num_list=[]
    while(card_number!=0):
    	remainder=card_number%10
    	num_list.append(remainder)
    	card_number//=10
    num_list=num_list[::-1]
    if len(num_list)==16:
    	num_list1=[]
    	num_list2=[]
    	for index in range(-2,-17,-2):
    		num_list1.append(num_list[index])
    	num_list1=num_list1[::-1]
    	for index in range(-1,-16,-2):
    		num_list2.append(num_list[index])
    	num_list2=num_list2[::-1]
    	for index in range(len(num_list1)):
    		num_list1[index]=num_list1[index]*2
    	for index in range(len(num_list1)):
    		if num_list1[index]>9:
    			num=num_list1[index]
    			sum_of_digits=0
    			while(num!=0):
    				remainder=num%10
    				sum_of_digits+=remainder
    				num//=10
    			num_list1[index]=sum_of_digits
    	summation_of_list1=0
    	summation_of_list2=0
    	for index in range(len(num_list1)):
    		summation_of_list1+=num_list1[index]
    	for index in range(len(num_list2)):
    		summation_of_list2+=num_list2[index]
    	if (summation_of_list2+summation_of_list1)%10==0:
    		return True
    return False

card_number=5239512608615007  #4539869650133101  #1456734512345698 #1456734512345698 #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
