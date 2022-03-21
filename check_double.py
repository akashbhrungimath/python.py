#lex_auth_01269441810970214471

def check_double(number):
    flag=True
    number_digit_list=[]
    double_number=2*number
    double_number_digit_list=[]
    while(number!=0):
        remainder=number%10
        number_digit_list.append(remainder)
        number//=10
    while(double_number!=0):
        remainder=double_number%10
        double_number_digit_list.append(remainder)
        double_number//=10
    if len(number_digit_list)==len(double_number_digit_list):
        for index in range(len(number_digit_list)):
            if number_digit_list[index] not in double_number_digit_list or double_number_digit_list[index] not in number_digit_list:
                flag=False
    else:
        flag=False
    return flag

#Provide different values for number and test your program
print(check_double(2))
