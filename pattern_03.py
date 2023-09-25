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
    pattern = ''
    for i in range(k):
        pattern += (f"{i * ' '}{(k-i) * '*'}\n")

    return pattern

# End-of-file (EOF)
