# To create a function that prints 
# *****
#  ****
#   ***
#    **
#     *

def patter3 ():
    
    k = 5
    for i in range(k):
        print (f"{i * ' '}{(k-i) * '*'}")


patter3 ()    