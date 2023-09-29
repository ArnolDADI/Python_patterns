"""
To create a funtion that prints pascal's triangle
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""
from math import factorial

def pattern_num_04():
    """ FUnction to return pascal' triangle"""
    pattern = ''
    for i in range (5):
        pattern += (5-i+1) * ' '
        for j in range (i+1):
            pattern += f"{factorial(i)//(factorial(j)*factorial(i-j))} "
        pattern += '\n'
    return pattern

# End-of-file (EOF)
