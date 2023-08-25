
#deleting files
""""
import os
os.remove("demofile2.txt")
"""
#Check if File exist:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")