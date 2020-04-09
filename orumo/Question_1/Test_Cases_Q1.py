"""
Created on Tue Apr  7 17:09:31 2020

@author: Arun_Arun
"""
import unittest
from whtroverlap import whtroverlap

class Testswhtroverlap(unittest.TestCase):
    # Testing cases for two lines on x-axis whether they overlap

	#CASE-1: WHEN THE LINES ENTERED ARE IN INCRESING ORDER
    
    def test_overlap_Positive(self):
        First_Line=[1, 5]
        second_Line=[3, 6]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[1, 5] & [3, 6] overlaps on x-axis")

    def test_doesnt_Overlap_Positive(self):
        First_Line=[1, 5]
        second_Line=[6, 8]
        output = whtroverlap(First_Line, second_Line)        
        self.assertEqual(output, "[1, 5] & [6, 8] doesnt overlaps on x-axis")

    def test_overlap_Negative(self):
        First_Line=[-5, -1]
        second_Line=[-6, -2]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[-5, -1] & [-6, -2] overlaps on x-axis")

    def test_doesnt_Overlap_Negative(self):
        First_Line=[-5, -1]
        second_Line=[-8, -6]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[-5, -1] & [-8, -6] doesnt overlaps on x-axis")
		
##float values

    def test_overlap_float(self):
        First_Line=[1.23, 6.45]
        second_Line=[6.44, 8.95]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[1.23, 6.45] & [6.44, 8.95] overlaps on x-axis")
		
    def test_doesnt_Overlap_float(self):
        First_Line=[2.34, 6.72]
        second_Line=[6.73, 9.44]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[2.34, 6.72] & [6.73, 9.44] doesnt overlaps on x-axis")

##integers

    def test_overlap_Integers(self):
        First_Line=[-1, 6]
        second_Line=[1, -3]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[-1, 6] & [1, -3] overlaps on x-axis")
		
##Origin

    def test_overlap_origin(self):
        First_Line=[0, 0]
        second_Line=[0, 0]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[0, 0] & [0, 0] overlaps on x-axis")

##Postive for first line and Negative for second line

    def test_doesnt_Overlap_Positivenegative(self):
        First_Line=[-1, -6]
        second_Line=[1, 6]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[-1, -6] & [1, 6] doesnt overlaps on x-axis")
		
		
	#CASE-2: WHEN THE LINES ENTERED ARE IN DECREASING ORDER


    def test_overlap_Positive_Decreasingorder(self):
        First_Line=[5, 1]
        second_Line=[8, 4]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[5, 1] & [8, 4] overlaps on x-axis")
		
    def test_doesnt_Overlap_Decreasingorder(self):
        First_Line=[6, 2]
        second_Line=[10, 7]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[6, 2] & [10, 7] doesnt overlaps on x-axis")
		
#Negative values

    def test_overlap_Negative_Decreasingorder(self):
        First_Line=[-5, -1]
        second_Line=[-6, -2]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[-5, -1] & [-6, -2] overlaps on x-axis")

    def test_doesnt_Overlap_Negative_Decreasingorder(self):
        First_Line=[-5, -1]
        second_Line=[-8, -6]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[-5, -1] & [-8, -6] doesnt overlaps on x-axis")
		
##float values

    def test_overlap_float_Decreasingorder(self):
        First_Line=[-6.45, -1.23]
        second_Line=[-8.95, -6.44]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[-6.45, -1.23] & [-8.95, -6.44] overlaps on x-axis")
		
    def test_doesnt_Overlap_float_Decreasingorder(self):
        First_Line=[-6.72, -2.34]
        second_Line=[-9.44, -6.73]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[-6.72, -2.34] & [-9.44, -6.73] doesnt overlaps on x-axis")

##integers

    def test_overlap_Integers_Decreasingorder(self):
        First_Line=[-6, 1]
        second_Line=[3, -1]
        output = whtroverlap(First_Line, second_Line)
        self.assertEqual(output, "[-6, 1] & [3, -1] overlaps on x-axis")

if __name__ == '__main__':
    unittest.main()