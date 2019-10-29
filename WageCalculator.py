'''
Created on 14 Sep 2016
Module to calculate my weekly wage
@author: Aidan
'''
hours = float(input("Please enter your hours worked: "))
days = float(input("How many days did you work?: "))
 
def basepay(hours):
    return hours * 9.80 #Min wage

def Breaks(days):  
    return days * (9.80/2) #30 mins removed for breaks each day worked.


print(basepay(hours) - Breaks(days) )  

print("Exiting program")