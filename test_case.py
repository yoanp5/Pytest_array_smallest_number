
import unittest
import heapq
import random
from class1 import*

Io = Iontra() # initialize class1


class Test_test_1(unittest.TestCase):
    def test_smallest_number(self) -> None:
        temp_array = Io.Random_array()
        result = Io.sort_array(temp_array)
        if not result:
            assert 0 == 0
        else:
            assert min(result) == result[0]

    def test_second_smallest_number(self) -> None:
        temp_array2 = Io.Random_array()
        result2 = Io.sort_array(temp_array2)
        if not result2:
            assert 0 == 0
        else:
            second_smallest = heapq.nsmallest(2, result2)[1] # find the second smallest number in the array
            assert second_smallest == result2[1]

    def test_nth_smallest_number(self) -> None:
        temp_array3 = Io.Random_array()
        result3 = Io.sort_array(temp_array3)
        nth = random.randint(0,len(result3))
        if not result3:
            assert 0 == 0
        elif nth == 0:
             assert min(result3) == result3[0]
        else:
            nth_smallest = heapq.nsmallest(nth, result3)[nth - 1] # find the nth smallest number in the array
            assert nth_smallest == result3[nth - 1]

if __name__ == '__main__':
    unittest.main()
