# https://byui-cse.github.io/cse111-course/lesson01/prove.html

# 01 Prove Milestone: Review Python

# Semih Aydin

# import the math module
import math 

# define constants for maximum allowed values
MAX_WIDTH = 999
MAX_ASPECT_RATIO = 999
MAX_DIAMETER = 999

# print a description and welcome
print("Welcome to tire volume calculator")
print("This program computes and outputs the volume of a tire")

# get the tire width, aspect ratio, and wheel diameter from the user
while True:
    try:
        tire_width = float(input("\nEnter the width of the tire in mm (ex 205): "))
        # check if the tire width is within the allowable range
        if tire_width < 0 or tire_width > MAX_WIDTH:
            # raise a ValueError if the tire width is not within the allowable range
            raise ValueError
        tire_aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
        # check if the tire aspect ratio is within the allowable range
        if tire_aspect_ratio < 0 or tire_aspect_ratio > MAX_ASPECT_RATIO:
            # raise a ValueError if the tire aspect ratio is not within the allowable range
            raise ValueError
        wheel_diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
        # check if the wheel diameter is within the allowable range
        if wheel_diameter < 0 or wheel_diameter > MAX_DIAMETER:
            # raise a ValueError if the wheel diameter is not within the allowable range
            raise ValueError
        
        # calculate the volume of the tire
        volume = (((math.pi * tire_width ** 2) * tire_aspect_ratio) * (tire_width * tire_aspect_ratio + (2540 * wheel_diameter))) / 10000000000
        
        # print the volume of the tire to the user
        print(f"\nThe approximate volume is {volume:.2f} liters")
        
        # exit the while loop since we have valid input from the user
        break
    
    except ValueError:
        # catch any invalid input and print an error message
        print("\nInvalid input. Please enter a valid number. (values must be between 0 and 999)")

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# open a text file named volumes.txt in append mode
with open("volumes.txt","at") as volumes:

    # print the required information to the file
    # Use an f-string to print only the date
    # part of the current date and time.
    print(f"\n{current_date_and_time:%Y-%m-%d}, {tire_width}, {tire_aspect_ratio}, {wheel_diameter}, {volume:.2f}", file = volumes)

while True:
    try:
        # ask the user if they want to buy the tire
        buy = input("\nWould you like to buy the tire? (yes or no) ").lower()
        
        # check if the input is valid (either "yes" or "no")
        if buy != "yes" and buy != "no":
            raise ValueError("\nInvalid input, please enter 'yes' or 'no'")
        
        # if the user wants to buy the tire
        if buy == "yes": 
            # ask for their phone number
            phone_number = input("\nPlease provide us your number! Our experienced sales assistants will call you for the best offers! ")
            
            # remove any non-digit characters from the phone number
            phone_number = ''.join(filter(str.isdigit, phone_number))
            
            # check if the phone number has the correct length
            if len(phone_number) != 10 :
                raise ValueError("Your phone number should consist of 10 digits!! ")
            
            # print a thank you message
            print("\nThank you for choosing us!")
            
            # append the phone number to the volumes.txt file
            with open('volumes.txt', 'a') as volumes:
                print(phone_number, file=volumes)
            
            # exit the loop
            break
        
        # if the user does not want to buy the tire
        if buy == "no":
            # print a goodbye message
            print("\nThank you! Have a great day!")
            
            # exit the loop
            break
    
    # handle any value errors (e.g., invalid input or phone number)
    except ValueError as e:
        print(e)

            
