"""
To create a function that returns
*****##*****
****#  #****
***#    #***
**#      #**
*#        #*
**#      #**
***#    #***
****#  #****
*****##*****
"""

def pattern_10():
    """ Function to return the enclosed diamond"""
    j = 0
    pattern = ''
    for i in range (11):
        if i <= 5:
            pattern += f"{(6-i) * '*'}#{j*' '}#{(6-i) * '*'}\n"
            j += 2

        else:
            j -= 2
            pattern += f"{(i-4) * '*'}#{(j-2)*' '}#{(i-4) * '*'}\n"

    return pattern

# End-of-file (EOF)
