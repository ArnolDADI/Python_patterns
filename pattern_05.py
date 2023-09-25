"""
To create a function that prints
    *
   ***
  *****
 *******
*********
"""

def pattern():
    """ Function printing the pattern"""
    k = 5
    j = 1
    for i in range (k):
        print (f"{(k - i - 1) * ' '}{j * '*'}")
        j += 2


pattern()
# End-of-file (EOF)
