"""
To create a function to print
    *
   **
  ***
 ****
*****
"""

def pattern_04():
    """ Function printing the pattern_04"""
    k = 5
    for i in range (k):
        print (f"{(k - i -1) * ' '}{(i+1) * '*'}")


pattern_04()
# End-of-file (EOF)
