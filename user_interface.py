
from class1 import *
import sys

Io = Iontra() # initialize class1

# This is the interface that will guide the user throughout the testing process.

while True:
    Io.intro()
    Io.selection()
    print("Would you like to continue Press N to exit \n")
    Press = input()
    if Press == "N" or Press == "n":
        sys.exit()




        
