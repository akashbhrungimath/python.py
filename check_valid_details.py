#lex_auth_012694465248329728100

def validate_name(name):
    if name.isalpha() and len(name)<=15:
    	return True
    return False

def validate_phone_no(phno):
    if phno.isdigit() and len(phno)==10 and phno.count(phno[0])<10:
    	return True
    return False

def validate_email_id(email_id):
    if "@" not in email_id:
    	return False
    elif email_id.count("@")!=1:
    	return False
    elif not email_id.endswith(".com"):
    	return False
    elif (email_id.count(".com")!=1):
    	return False
    domain=""
    index=-5
    while(email_id[index]!="@"):
    	domain+=email_id[index]
    	index-=1
    domain_list=["gmail","yahoo","hotmail"]
    if domain[::-1] not in domain_list:
    	return False
    return True

def validate_all(name,phone_no,email_id):
    flag=True
    if (not validate_name(name)):
    	flag=False
    	print("Invalid Name")
    if (not validate_phone_no(phone_no)):
    	flag=False
    	print("Invalid phone number")
    if (not validate_email_id(email_id)):
    	flag=False
    	print("Invalid email id")
    if flag:
    	print("All the details are valid")
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9999999998", "tina@gmail.com")
