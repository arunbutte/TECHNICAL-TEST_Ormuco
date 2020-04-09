"""
Created on Tue Apr  7 17:09:31 2020

@author: Arun_Arun
"""
import unittest
from Compare import Compare

class Compare2String(unittest.TestCase):

##Negative input    
    def test_Negative_greater(self):
        output = Compare(-1.11, -1.52)
        self.assertEqual(output, "-1.11 is greater then -1.52")

    def test_Negative_lower(self):
        output = Compare(-2.11, -1.98)       
        self.assertEqual(output, "-2.11 is lower then -1.98")

    def test_Negative_equal(self):
        output = Compare(-5.23, -5.23)       
        self.assertEqual(output, "-5.23 is equal to -5.23")

##positive input    
    def test_Positive_greater(self):
        output = Compare(5.11, 1.52)
        self.assertEqual(output, "5.11 is greater then 1.52")

    def test_Positive_lower(self):
        output = Compare(6.22, 7.54)       
        self.assertEqual(output, "6.22 is lower then 7.54")

    def test_Positive_equal(self):
        output = Compare(10.12, 10.12)       
        self.assertEqual(output, "10.12 is equal to 10.12")


if __name__ == '__main__':
    unittest.main()