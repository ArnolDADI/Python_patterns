"""
To create a function that returns
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
"""

def pattern_num_03():
    """ Function to create the pattern"""
    pattern = ''

    for i in range (5):
        pattern += (4-i) * ' '
        for j in range (i+1):
            pattern += f"{i+1} "
        pattern += '\n'

    return pattern


# End-of-file (EOF)
