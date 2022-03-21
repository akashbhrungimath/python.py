#lex_auth_01269442963365068878

def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    if(is_prime(list_of_factors[-1],list_of_factors[-1]//2)):
        return list_of_factors[-1]
    else:
        list_of_factors.remove(list_of_factors[-1])
        largest_prime_factor=find_largest_prime_factor(list_of_factors)
        return largest_prime_factor

def find_f(num):
    list_of_factors=find_factors(num)
    largest_prime_factor=find_largest_prime_factor(list_of_factors)
    return largest_prime_factor

def find_g(num):
    sum_of_prime_factors=0
    for i in range(0,9):
        sum_of_prime_factors+=find_f(num+i)
    return sum_of_prime_factors

#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))
