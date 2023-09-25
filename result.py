""" 
To print all the pattern files starting with 'pattern_' in its name.
"""
import os
with open('pattern.md', 'w', encoding = 'utf-8') as f:
    for x in os.listdir():
        if x.startswith("pattern_"):
            # To get the name of the file
            patterns = x[:-3]
            
            try:
                mod =__import__(patterns)
                f.write(f"\n\n*{patterns}\n")
                func = getattr(mod, patterns)
                f.write(f"{func()}")
            except ImportError:
                print ("Error ", patterns)

# End-of-file (EOF)
