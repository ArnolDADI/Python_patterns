""" 
To print all the pattern files starting with 'pattern_' in its name.
"""
import os

for x in os.listdir():
    if x.startswith("pattern_"):
        # Prints only text file present in My Folder
        patterns = x[:-3]
        try:
            print (f"{patterns}\n")
            __import__(patterns)
            print ("\n*Success\n")
        except ImportError:
            print ("Error ", patterns)

# End-of-file (EOF)