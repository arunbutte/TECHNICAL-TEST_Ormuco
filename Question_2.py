"""
Created on Tue Apr  7 17:09:31 2020

@author: Arun_Arun
"""
from Compare import Compare
if __name__ == '__main__':
    try:
        
        print("enter the first string to compare")
        String1=float(input())
        print("enter the second string to compare")
        String2=float(input())

        output=Compare(String1, String2)
        print(output)
    
    except ValueError:
        print('\n')
        print('**' * 42)
        print('Please Enter only numbers\n'
              "Characters, strings are not allowed \n{0}".format('**' * 42))