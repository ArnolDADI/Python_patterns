"""
To create a function that returns
*
**
***
****
*****
****
***
**
*
"""

def pattern_07():
    """ Function to return the pattern"""
    pattern = ''
    for i in range(10):
        if i <= 5:
            pattern += f"{i * '*'}\n"
        else:
            j = 10-i
            pattern += f"{j * '*'}\n"

    return pattern

# End-of-line (EOF)
