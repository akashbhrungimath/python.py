#lex_auth_01269442114344550475

def is_palindrome(word):
    if len(word)<2:
        return True
    elif word[0].lower()!=word[-1].lower():
        return False
    else:
        return is_palindrome(word[1:-1])

#Provide different values for word and test your program
result=is_palindrome("Madam")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
