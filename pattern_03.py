"""
To create a function that prints
*****
 ****
  ***
   **
    *
"""

def pattern3 ():
    """ Function printing the pattern"""
    k = 5
    for i in range(k):
        print (f"{i * ' '}{(k-i) * '*'}")


pattern3()
# End-of-file (EOF)
