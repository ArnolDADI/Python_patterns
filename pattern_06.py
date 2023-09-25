"""
To create a function that return
*********
 *******
  *****
   ***
    *
"""

def pattern_06():
    """ Function printing the pattern_06"""
    pattern = ''
    for i in range(6):
        pattern += f"{i * ' '}{((9-(i*2)) * '*')}\n"
        
    return pattern

# End-of-file (EOF)