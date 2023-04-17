# https://byui-cse.github.io/cse111-course/lesson01/prove.html

# 01 Prove Milestone: Review Python

# Semih Aydin

# import the math module
import math 

# print a description and welcome
print("Welcome to tire volume calculator")
print("This program computes and outputs the volume of a tire")

# get the with, aspetct ratio of the tire and the diameter of  the wheel
while True:
    try:
        width = float(input("Enter the width of the tire in mm (ex 205): "))
        if width < 0 or width > 999:
            raise ValueError
        aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
        if aspect_ratio < 0 or aspect_ratio > 999:
            raise ValueError
        diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
        if diameter < 0 or diameter > 999:
            raise ValueError
        
        # compute the volume of the tire
        volume = (((math.pi*width**2)*aspect_ratio)*(width*aspect_ratio + (2540*diameter)))/10000000000
        
        # print the volume of the tire for the user to see
        print(f"\nThe approximate volume is {volume:.2f} liters")
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer. (values must be between 0 and 999)")