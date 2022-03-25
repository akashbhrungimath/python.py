#lex_auth_01269446157664256093
import math
def check_prime(number):
    for i in range(2,int(math.sqrt(number)+1)):
    	if number%i==0:
    		return False
    return True

def rotations(num):
    str_num=str(num)
    list_of_circular_nums=[]
    for i in range(len(str_num)):
    	list_of_circular_nums.append(int(str_num))
    	char=str_num[0]
    	str_num=str_num.replace(str_num[0],"",1)
    	str_num+=char
    return list_of_circular_nums
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]

def get_circular_prime_count(limit):
    prime_nums=[]
    list_of_circular_prime_nums=[]
    for i in range(2,limit):
    	if check_prime(i):
    		prime_nums.append(i)
    for num in prime_nums:
    	list_of_nums=rotations(num)
    	for number in list_of_nums:
    		if check_prime(number):
    			flag=True
    		else:
    			flag=False
    			break
    	if flag:
    		list_of_circular_prime_nums.append(num)
    return len(list_of_circular_prime_nums)

#Provide different values for limit and test your program
print(get_circular_prime_count(100))
