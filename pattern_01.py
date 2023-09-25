""" To create a function that prints
*
**
***
****
*****
"""

def pattern_01():
    """ Function printing the pattern_01"""
    pattern = ''
    for i in range(0, 6):
        pattern += f"{i * '*'}\n"

    return pattern

# End-of-file (EOF)
