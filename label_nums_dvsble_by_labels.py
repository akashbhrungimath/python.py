#lex_auth_0127136209566679041189

def check_numbers(num1,num2):
    num_list=[]
    count=0
    temp1=num1
    while(num1<=num2):
    	temp=temp1
    	while(temp<=num2):
    		if(temp==num1):
    			temp+=1
    			continue
    		elif(num1%temp==0):
    			num_list.append(num1)
    			count+=1
    			break
    		temp+=1
    	num1+=1
    num_list=set(num_list)
    return [num_list,count]

num1=10
num2=30
print(check_numbers(num1, num2))
