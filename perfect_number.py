#lex_auth_01269446533799116898
import math

def find_factors(number):
    factors=[1]
    for num in range(2,int(math.sqrt(number)+1)):
        if(number%num==0):
            factors.append(num)
            factors.append(number//num)
    return factors

def check_perfect_number(number):
    if(number==1):
        return False
    factors_of_number=find_factors(number)
    sum_of_factors=0
    for num in factors_of_number:
        sum_of_factors+=num
    if(sum_of_factors==number):
        return True
    else:
        return False

def check_perfectno_from_list(no_list):
    perfect_no_list=[]
    for num in no_list:
        flag=check_perfect_number(num)
        if(flag):
            perfect_no_list.append(num)
    return perfect_no_list

perfectno_list=check_perfectno_from_list([18,6,4,2,1,28,496])
print(perfectno_list)
