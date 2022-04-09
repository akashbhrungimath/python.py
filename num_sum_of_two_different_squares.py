#lex_auth_0127136357122129921205

def check_squares(number):
    a=1
    while(a**2<=number):
    	b=1
    	while(a**2+b**2<=number):
    		if(a**2+b**2==number):
    			return True
    		b+=1
    	a+=1
    return False

number=68
print(check_squares(number))
