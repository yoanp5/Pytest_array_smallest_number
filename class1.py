
import random

set_numb = [] #empty array

class Iontra:

    def __init__(self):
        pass

    def intro(self):
        print ("Hi please select your desire function:\n 1 - Return smallest number in the array. \n 2 - retrun the second smallest number in the array. \n 3 - return the nth smallest number in the array")



    def create_array(self):
        print("Please select between the two option: \n 1 - Randomize array numbers. \n 2 - User input array numbers")
        while True:
            try:
                select = int(input("Enter a number betwen 1-2:\n"))
            except ValueError:
                print ("Please enter a integer between 1 - 2 \n")
                continue
            if select < 1 or select > 2:
                print ("Please enter a number between 1 - 2 \n")
                continue
            else:
                break
        if select == 1:
            self.Random_array()
        elif select == 2:
            self.User_array()



    def sort_array (self, set_numb):

        #can definitively do Set_numb.sort() here but wanted to try to sort it myself
        
        temp_array = [] 
        while set_numb:
            minimum = set_numb[0]
            for x in set_numb:
                if x < minimum:
                    minimum = x
            temp_array.append(minimum) # adding sorted number to the temporary array
            set_numb.remove(minimum) # removing number to the original array in order to populate it with sorted one.
        set_numb = temp_array.copy()
        return set_numb



    def Random_array(self) -> set_numb:
        x = random.randint(0,15) #getting a random size array
        for i in range(x):
            set_numb.append(random.randint(0,100)) # populate the Array with Random numbers
        return set_numb



    def User_array(self) -> set_numb:
        while True:
            try:
                size = int(input("Please enter the size of the array: \n"))
            except ValueError:
                print ("Please enter an integer \n")
                continue
            else:
                break

        for i in range(size):
            while True:
                try:
                    set_numb.append(int(input(f"Please enter a value for {i} : \n"))) # populate the array with user numbers
                except ValueError:
                    print ("Please enter an integer \n")
                    continue
                else:
                    break

        return set_numb



    def selection(self):
        result = []
        while True:
            try:
                select = int(input("Enter a number betwen 1-3:\n"))
            except ValueError:
                print ("Please enter a integer between 1 - 3 \n")
                continue
            if select < 1 or select > 3:
                print ("Please enter a number between 1 - 3 \n")
                continue
            else:
                break
                            #Match and case keyword can be use here for different implementation but in case the python enviroment does have/support Python 3.10 I went with an if statement
        if select == 1:
            self.create_array()
            print("Your Array is : \n", set_numb)
            result = self.sort_array(set_numb)
            print("The sorted Array is : \n", result)
            if not result:
                return print("The Array is empty \n")
            else:
                return print("The Smallest number in the Array is : \n", result[0])
        elif select == 2:
            self.create_array()
            print("Your Array is : \n", set_numb)
            result = self.sort_array(set_numb)
            print("The sorted Array is : \n", result)
            if not result:
                return print("The Array is empty \n")
            else:
                return print("The second Smallest number in the Array is : \n", result[1])
        elif select == 3:
             self.create_array()
             print("Your Array is : \n", set_numb)
             result = self.sort_array(set_numb)
             print("The sorted Array is : \n", result)
             if not result:
                return print("The Array is empty \n")
             else:
                while True:
                    try:
                        select = int(input("Enter the nth Array to be returned starting at 0 \n"))
                    except ValueError:
                        print ("Please enter an integer between 0 -  \n", len(result))
                        continue
                    if select < 0 or select < len(result):
                        break
                    else:
                        print ("Please enter a number between 0 -  \n", len(result))
        return print("The ", select, " Smallest number in the Array is : \n", result[select])
