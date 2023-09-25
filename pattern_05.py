"""
To create a function that prints
    *
   ***
  *****
 *******
*********
"""

def pattern_05():
    """ Function printing the pattern_05"""
    k = 5
    j = 1
    for i in range (k):
        print (f"{(k - i - 1) * ' '}{j * '*'}")
        j += 2


#pattern_05()
# End-of-file (EOF)
