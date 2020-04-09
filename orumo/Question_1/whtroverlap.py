"""
Created on Wed Apr  8 11:53:11 2020

@author: abutte2
"""
def whtroverlap(First_Line, second_Line):
    SFL=list(First_Line)
    SFL.sort()
    SSL=list(second_Line)
    SSL.sort()
    output=str(First_Line) + " & "+ str(second_Line) + "doesnt overlaps on x-axis"
    if ((SSL[1]<SFL[0]) or (SFL[1]<SSL[0])):
        output=str(First_Line) + " & "+ str(second_Line) + " doesnt overlaps on x-axis"
    else:
        output=str(First_Line) + " & " + str(second_Line) + " overlaps on x-axis"     
    return output
            
