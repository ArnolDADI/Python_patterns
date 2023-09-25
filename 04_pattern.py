# To create a function to print 
#     *
#    **
#   ***
#  ****
# *****

def patter4 ():
    
    k = 5
    for i in range (k):
        print (f"{(k - i -1) * ' '}{(i+1) * '*'}")


patter4 ()    