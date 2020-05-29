#!/usr/bin/env python3
# Michael Fanous Cs87 Project 5
#GPA calculator!

totalpoints = 0
totalunits = 0

def legal(amount,lowerbound,upperbound):
    #setting up way to check validity of units and grades
    if(amount >= lowerbound and amount <= upperbound):
        return True
    else:
        return False

def display():
    #display the 3 options to the user
    print("1. Input grade received and number of units taken: ")
    print("2. Show GPA")
    print("3. Quit Program")
    main_input = int(input('Enter 1,2, or 3: '))
    if(main_input == 1 or main_input == 2 or main_input == 3):
        return main_input
    else:
        return -1


def main():
   main_input = display()
   if(main_input == 1):
        global totalpoints
        global totalunits	
        grade = int(input("Grade Enter as a number please!(A=4,B=3,C=2,D=1,F=0): "))
        units = int(input("Units: "))
        # here we used legal which was defined above to check the validity
        bool_grades=legal(grade,0,4)
        bool_units=legal(units,0,5)
        if(bool_grades == True and bool_units == True):
            totalpoints = (totalpoints+(grade*units))
            totalunits =(totalunits+units)
        else:
             print("Error,invalid input")
        main()
   elif(main_input == 2):
        #If user asks for GPA before classes are entered it tells them to enter classes and gives menu again:
        if totalunits == 0:
            print("Please enter classes!")
            main()
        # Here is where we show a formula for gpa
        gpa=(totalpoints)/(totalunits)
        print("GPA =",gpa)
        main()
   #we have setup any entry besides "1","2", or "3" to return -1 which throws an error and gives them menu options again
   elif(main_input == -1):
         print("Entered option is invalid, try again")
         main() 

   elif(main_input == 3):
        print("Thanks for using my GPA calculator good luck in your studies!")
        exit()





main()

