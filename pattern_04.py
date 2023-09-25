"""
To create a function to print
    *
   **
  ***
 ****
*****
"""

def pattern4 ():
    """ Function printing the pattern"""
    k = 5
    for i in range (k):
        print (f"{(k - i -1) * ' '}{(i+1) * '*'}")


pattern4()
# End-of-file (EOF)
