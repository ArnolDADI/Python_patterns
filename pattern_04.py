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
    pattern = ''
    for i in range (k):
        pattern += (f"{(k - i -1) * ' '}{(i+1) * '*'}\n")

    return pattern

# End-of-file (EOF)
