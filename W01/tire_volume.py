# https://byui-cse.github.io/cse111-course/lesson01/prove.html

# 01 Prove Milestone: Review Python

# Semih Aydin

# import the math module
# import the math module
import math 

# define constants for maximum allowed values
MAX_WIDTH = 999
MAX_ASPECT_RATIO = 999
MAX_DIAMETER = 999

# print a description and welcome
print("Welcome to tire volume calculator")
print("This program computes and outputs the volume of a tire")

# get the width, aspect ratio of the tire and the diameter of the wheel
while True:
    try:
        tire_width = float(input("Enter the width of the tire in mm (ex 205): "))
        if tire_width < 0 or tire_width > MAX_WIDTH:
            raise ValueError
        tire_aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
        if tire_aspect_ratio < 0 or tire_aspect_ratio > MAX_ASPECT_RATIO:
            raise ValueError
        wheel_diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
        if wheel_diameter < 0 or wheel_diameter > MAX_DIAMETER:
            raise ValueError
        
        # compute the volume of the tire
        volume = (((math.pi * tire_width ** 2) * tire_aspect_ratio) * (tire_width * tire_aspect_ratio + (2540 * wheel_diameter))) / 10000000000
        
        # print the volume of the tire for the user to see
        print(f"\nThe approximate volume is {volume:.2f} liters")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number. (values must be between 0 and 999)")