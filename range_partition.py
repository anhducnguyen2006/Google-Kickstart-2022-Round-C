# =============================================================================
# ROUND C EXERCISE 2 - Range Partition
# Google Kickstart 2022
#
# Programming language: Python
#
# Thursday 08/26/2022 
#
# Name: Anh Duc Nguyen
# Age: 16
# =============================================================================


def solve(n,x,y,i):
    # counting n! (adding all the number from 1 to n)
    s = n*(n+1)/2
    
    # if s is not divisible by the sum of proportions (x+y),
    # print "IMPOSSIBLE"
    if s%(x+y)!=0:
        # this is the output format that kickstart requires us to print out. 
        print("Case #{}: {}".format(i, "IMPOSSIBLE"))
    else:
        # else -> create an array with 
        # numbers Alan will pick
        ans=[]
        # here scan through all the numbers 
        # from 1 to n
        for k in range(1,n+1):
            # check if the sum of numbers Alan picked so far
            # is less than the desired amount which is the xth 
            # portion of s
            if sum(ans)<s*x/(x+y): 
                # append, even if, after adding k, 
                # the sum will be bigger than the desired xth
                # portion of s
                ans.append(k)
        # this formula checks, if the sum of numbers
        # in this array exceeds the desired sum (s*x/(x+y))
        # if so, find a number in that array that
        # by deleting it, the sum of the array will 
        # be equal to the desired xth portion of s.
        # this is guaranteed to success because
        # the difference of the sum of the array and
        # the desired amount is always smaller than the last
        # k we added (eg. the last k we added was 11 and 
        # the difference is always less than k)
        if sum(ans)>s*x/(x+y):
            ans.remove(sum(ans)-(s*x/(x+y)))
        
        # this is the output format that kickstart requires us to print out. 
        print("Case #{}: {}".format(i, "POSSIBLE"))
        print(len(ans))
        for j in ans:
            print(j, end=" ")
        print("")

# this is the output format that kickstart requires us to print out. 
T=int(input("Number of test: "))
for i in range(1,T+1):
    n,x,y=[int(i) for i in input("Give n,x,y: ").split()]
    solve(n,x,y,i)