#            This program's objective is to return the first, second, and nth smallest numbers into a random or user-generated array of an integer number.
#
#
#   Programmer: Yannick Ngole
#   Recruiter: Neil McCullough
#
# For any information or concern please email: Yannickpenda@gmail.com
#
#
#
#

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




        
