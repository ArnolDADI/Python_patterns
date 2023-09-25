""" 
To print all the pattern files starting with 'pattern_' in its name.
"""
import os

# To create a new file every time the file is run and check for replaced, added or removed files
with open('pattern.txt', 'w', encoding = 'utf-8') as f:
    for x in os.listdir():
        if x.startswith("pattern_"):
            patterns = x[:-3]       # To get the name of the file

            try:
                mod =__import__(patterns)
                f.write(f"\n\n*{patterns}\n")
                func = getattr(mod, patterns)
                f.write(f"{func()}")
            except ImportError:
                print ("Error ", patterns)

# End-of-file (EOF)
