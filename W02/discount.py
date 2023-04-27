# https://byui-cse.github.io/cse111-course/lesson02/teach.html

# 02 Team Activity: Calling Functions

# Semih Aydin
# To get current date and time we need to use the datetime library
from datetime import datetime

# the discount rate is 10% and the sales tax rate is %6.
discount_rate = 0.1
sales_tax_rate =0.06

# return the current date and time as a date time object 
current_date = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date.weekday()

# welcoming the customer
print("Welcome to shopping calculator ")

if day_of_week == 1 or day_of_week == 2:
    print(f"Today is your lucky day and you will have %10 of discount! ")

# handling errors by entering to a loop
while True:
    try:
        # getting the user input
        subtotal = float(input("Please enter the subtotal: "))
        # raising a value error for negative amounts
        if subtotal < 0:
            raise ValueError
        # if the subtotal is greater than 50 and the date is Tue. or Wed. compute disc.
        if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
            discount_amount = subtotal*discount_rate
            print(f"Discount amount:{discount_amount:.2f}")
            subtotal = subtotal - discount_amount

        # Compute the sales tax and total amount then display both
        sales_tax = subtotal*sales_tax_rate
        total = subtotal + sales_tax
        print(f"Sales tax amount: {sales_tax:.2f}")
        print(f"Total : {total:.2f}")
        break
    # accepting only numeral values
    except ValueError:
        print("Invalid input for subtotal. Please enter a number! ")




            
        

        












