"""
To create a function to print
    *
   **
  ***
 ****
*****
"""

def pattern():
    """ Function printing the pattern"""
    k = 5
    for i in range (k):
        print (f"{(k - i -1) * ' '}{(i+1) * '*'}")


pattern()
# End-of-file (EOF)
