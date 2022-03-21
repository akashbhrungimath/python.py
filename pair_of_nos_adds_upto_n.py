#lex_auth_01269438594930278448

def find_pairs_of_numbers(num_list,n):
    count=0
    num_set=set(num_list)
    for num1 in num_set:
        for num2 in num_set:
            if num1+num2==n:
                count+=1
    return count//2

num_list=[1, 2, 7,4, 5, 6,0,3]
n=6
print(find_pairs_of_numbers(num_list,n))
