"""
To create a function to return 
1
2   3
4   5   6
7   8   9   10
11  12  13  14  15
"""

def pattern_num_01():
    """ Function to return the pattern"""
    pattern = ''
    k = 1
    for i in range (6):
        for j in range (i):
            pattern += f"{k}\t"
            k += 1
        pattern += "\n"

    return pattern

# End-of-file (EOF)
