#!/usr/bin/env python3
# Michael Fanous Cs87 Project 4 
#Created on January 15
#Last edit January 18th

def tempconverter(fahrenheit):
#find relation between celsius and fahrenheit and create formula
    celsius = (fahrenheit - 32) * (5/9)
    return celsius
#define the conversion of mph to mps
def speedconverter(mph):
   #find relation between mph to mps to create formula
    mps = (mph / (2.237))
    return mps

def main():
   #give user options
    print("enter 1 to convert Fahrenheit temperature to Celsius")
    print("enter 2 to convert speed from Miles per hour to meters per second")
   #take in user input   
    main_input = int(input('Enter your input: '))#converting input to integer
    if main_input == 1:
        fahrenheit = float(input('Please enter temperature in Fahrenheit: '))
       #if fahrenheit == ""
        #    print("Restart the program and enter a value for Fahrenheit")
        celsius = tempconverter(fahrenheit)
        print("The degrees in Celsius is",celsius,"degrees")
    elif main_input == 2:
        mph = float(input('Please enter speed in mph: '))
       #if mph == ""
        #    print("Restart the program and enter a value for miles per hour")
        mps = speedconverter(mph)
        print(mph,"miles","is",mps,"meters per second")
    else:
        #tells user to restart rather than purely gives error because we havent set something to auto restart programs
        print("Error,please restart the program and enter 1 or 2")

main()

# How would I tell the user to restart the program if they enter "" for a user input for temperature or mph?
