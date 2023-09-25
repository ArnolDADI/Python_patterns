"""
To create a funtion that prints
*****
****
***
**
*
"""

def pattern_02():
    """ Function printing the pattern_02"""
    pattern = ''
    for i in range(5, 0, -1):
        pattern += f"{i * '*'}\n"

    return pattern

# End-of-file (EOF)
