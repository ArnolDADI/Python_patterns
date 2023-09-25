"""
To create a function that prints
*****
 ****
  ***
   **
    *
"""

def pattern_03():
    """ Function printing the pattern_03"""
    k = 5
    for i in range(k):
        print (f"{i * ' '}{(k-i) * '*'}")


pattern_03()
# End-of-file (EOF)
