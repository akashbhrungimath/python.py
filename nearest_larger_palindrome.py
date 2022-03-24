#lex_auth_01269443664174284882
import math
def nearest_palindrome(number):
    palindrome=0
    temp=number
    index=0
    while(temp!=0):
    	remainder=temp%10
    	palindrome+=(remainder*math.pow(10,index))
    	temp//=10
    	index+=1
    if palindrome==number:
    	number+=1
    list_number=[]
    number
    while(number!=0):
    	remainder=number%10
    	list_number.append(remainder)
    	number//=10
    list_number=list_number[::-1]
    index1=0
    index2=len(list_number)-1
    while(index1<index2):
    	if list_number[index1]==list_number[index2]:
    		index1+=1
    		index2-=1
    	elif list_number[index1]>list_number[index2]:
    		list_number[index2]=list_number[index1]
    		index1+=1
    		index2-=1
    	else:
    		list_number[index2-1]+=1
    		list_number[index2]=list_number[index1]
    		index1+=1
    		index2-=1
    for index in range(0,len(list_number)):
    	number+=int(list_number[index]*math.pow(10,index))
    return number

number=99
print(nearest_palindrome(number))
