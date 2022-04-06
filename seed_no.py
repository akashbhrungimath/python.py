#lex_auth_0127135857243832321154

def seed_no(number,ref_no):
    list_of_digits_number=[]
    temp=number
    while(temp!=0):
    	remainder=temp%10
    	list_of_digits_number.append(remainder)
    	temp//=10
    for num in list_of_digits_number:
    	number*=num
    if number==ref_no:
    	return True
    return False

number=45
ref_no=1000
print(seed_no(number,ref_no))
