# https://byui-cse.github.io/cse111-course/lesson01/check.html

# 01 Checkpoint: Review Python

# Semih Aydin

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

print("Welcome to heart rate calculator")

while True:
    try:
        # get the user input
        age = int(input("Please enter your age: "))
        if age < 0 or age > 99:
            raise ValueError
        max_rate = 220 - age
        highest = max_rate * 0.85
        lowest = max_rate * 0.65
        # display the result to the user
        print(f"When you exercise to strengthen your heart, you should keep your heart rate between {lowest:.0f} and {highest:.0f} beats per minute")
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for age (Age must be between 0 and 99).")
