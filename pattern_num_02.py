"""
To create a function that returns
1
22
333
4444
55555
"""

def pattern_num_02():
    """ Function to return the pattern"""
    pattern = ''

    for i in range (6):
        for j in range (i):
            pattern += f"{i}\t"
        pattern += "\n"

    return pattern

# End-of-file (EOF)
