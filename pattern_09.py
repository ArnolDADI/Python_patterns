"""
To create a function that returns
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""

def pattern_09():
    """ Function to create diamond pattern"""
    pattern = ''
    j = -1
    for i in range (10):
        if i < 5:
            j += 2
            pattern += (f"{(4 - i) * ' '}{j * '*'}\n")

        else:
            j -= 2
            pattern += f"{(i-4) * ' '}{j * '*'}\n"

    return pattern

# End-of-file (EOF)
