"""
Created on Tue Apr  7 17:09:31 2020

@author: Arun_Arun
"""

from whtroverlap import whtroverlap
if __name__ == '__main__':
    try:
        
        First_Line=[] #creating a empty for first line
        second_Line=[] #creating a empty for second line
        print("enter the first line (x1,x2) on the x-axis ,SEPERATED by a space")
        First_Line=list(map(int, input().split())) 
        First_Line=tuple(First_Line)
        print("enter the second line (x1,x2) on the x-axis ,SEPERATED by a space")
        second_Line=list(map(int, input().split()))
        second_Line=tuple(second_Line)
        
        output=whtroverlap(First_Line, second_Line) #using the funtion to determine whether the two line are overlapping
        print(output)
    except ValueError:
        print('\n')
        print('**' * 42)
        print('Please Enter only numbers\n'
              "Characters, strings are not allowed \n{0}".format('**' * 42))