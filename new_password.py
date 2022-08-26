# =============================================================================
# ROUND C EXERCISE 1 - New Password
# Google Kickstart 2022
#
# Programming language: Python
#
# Thursday 08/26/2022 
#
# Name: Anh Duc Nguyen
# Age: 16
# =============================================================================

# NO REGEX

def solve(n,s):
    # create all requirements possible: 
    
    # special character
    sc = ["#", "@", "*", "&"]
    
    # small letters from the alphabet
    alphasmal = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # capital letters from the alphabet
    alphabig =  ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    # numbers possible
    num = ['0','1','2','3','4','5','6','7','8','9']
    
    # To check if the password (string) contains such characters
    
    # r1 for numbers
    # r2 for capital letters
    # r3 for small letters
    # r4 for special characters
    
    r1,r2,r3,r4=False,False,False,False
    
    # loop through all the elements of the password
    # change r1/r2/r3/r4 to True if the current letter is in one of 
    # the four requirements
    for i in s: 
        if i in num:
            r1=True
        if i in alphabig:
            r2=True
        if i in alphasmal:
            r3=True
        if i in sc:
            r4=True
            
    #if not, add one of their elements, any is fine 
    if r1==False:
        s+="1"
    if r2==False:
        s+=alphabig[0]
    if r3==False:
        s+=alphasmal[0]
    if r4==False:
        s+=sc[0]
        
    # lastly, check if the length of the password fulfilling all 
    # the requirements is greater than 7, if not,
    # add anything from the four requirements
    if len(s)<7:
        for j in range(7-len(s)):
            s+="1"
    return s
            
# this is the output format that kickstart requires us to print out. 
T = int(input())
for i in range(1,T+1):
    n=int(input())
    s=input()
    print("Case #{}: {}".format(i,solve(n,s)))