#lex_auth_0127136447430656001216

def convert_to_roman(num):
    roman_num=""
    while(num!=0):
    	if num>=1000:
    		roman_num+="M"
    		num-=1000
    	elif num<1000 and num>=900:
    		roman_num+="CM"
    		num-=900
    	elif num<900 and num>=500:
    		roman_num+="D"
    		num-=500
    	elif num<500 and num>=400:
    		roman_num+="CD"
    		num-=400
    	elif num<400 and num>=100:
    		roman_num+="C"
    		num-=100
    	elif num<100 and num>=90:
    		roman_num+="XC"
    		num-=90
    	elif num<90 and num>=50:
    		roman_num+="L"
    		num-=50
    	elif num<50 and num>=40:
    		roman_num+="XL"
    		num-=40
    	elif num<40 and num>=10:
    		roman_num+="X"
    		num-=10
    	elif num==9:
    		roman_num+="IX"
    		num-=9
    	elif num<9 and num>=5:
    		roman_num+="V"
    		num-=5
    	elif num==4:
    		roman_num+="IV"
    		num-=4
    	elif num<4 and num>=1:
    		roman_num+="I"
    		num-=1
    	else:
    		return -1
    return roman_num

for num in range(1,5000):    
    print(num," : ",convert_to_roman(num))
