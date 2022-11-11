#Description: This program objective is to return the first, second and nth smallest number into a random or user generated array of integer number.
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
import heapq

Io = Iontra()


while True:
    #Io.intro()
    #Io.selection()
    #print("Would you like to continue Press N to exit \n")
    #Press = input()
    temp_array3 = Io.Random_array()
    result3 = Io.sort_array(temp_array3)
    nth = random.randint(0,len(result3))
    if not result3:
        assert 0 == 0
    else:
         nth_smallest = heapq.nsmallest(nth, result3)[nth - 1]
         assert nth_smallest == result3[nth - 1]
    print("Would you like to continue Press N to exit \n")
    Press = input()
    if Press == "N" or Press == "n":
        sys.exit()



   



        
