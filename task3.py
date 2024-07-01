#!/usr/bin/python3

#Printing the calendar of a given month and year

import calendar  
year = int(input("Enter the Year: ")) 
month = int(input("Enter the month: "))    
print("The Calendar: ", calendar.month(year, month))  
