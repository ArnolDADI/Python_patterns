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
    pattern = ''
    for i in range (k):
        pattern += (f"{(k - i - 1) * ' '}{j * '*'}\n")
        j += 2

    return pattern

# End-of-file (EOF)
