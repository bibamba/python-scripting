# import os module
import os
import sys

# command line argument
args = sys.argv
if len(args) != 3:
    raise Exception("You must enter a source and target directory")
source, target = args[1:] 

# mode 
mode = 0o666

# Path
paths = os.path.join(source, target)

# Create the directory
os.mkdir(paths, mode)
print("Directory '% s' created" % target)