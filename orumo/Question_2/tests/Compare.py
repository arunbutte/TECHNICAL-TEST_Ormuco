"""
Created on Tue Apr  7 17:09:31 2020

@author: Arun_Arun
"""
def Compare(String1, String2):
    if(String1>String2):
        output=str(String1)+ " is greater then " +str(String2)
    elif(String1<String2):
        output=str(String1)+ " is lower then " +str(String2)
    elif(String1==String2):
        output=str(String1)+ " is equal to " +str(String2)
    return output

            
    