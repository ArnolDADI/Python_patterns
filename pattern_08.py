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

def pattern_08():
    """ Function to return the pattern"""
    pattern = ''
    for i in range (10):
        if i <= 5:
            pattern += f"{(5-i) * ' '}{(i) * '*'}\n"
        else:
            pattern += f"{(i-5) * ' '}{(10-i) * '*'}\n"


    return pattern

# End-of-file (EOF)
