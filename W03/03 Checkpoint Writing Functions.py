# https://byui-cse.github.io/cse111-course/lesson03/check.html

# 03 Checkpoint: Writing Functions

# Semih Aydin

# Define the max value for end, start and fuel consumption value
MAX_START = 999999
MAX_END = 999999
MAX_FUEL = 999

def main():
    # Entering to a loop to verify user input
    while True:
        try:
            # Get an odometer value in U.S. miles from the user.
            start_miles = float(input("Enter the first odometer reading (miles): "))
            if start_miles < 0 or start_miles > MAX_START:
                raise ValueError
            
    # Get another odometer value in U.S. miles from the user.
            end_miles = float(input("Enter the second odometer reading (miles): "))
            if end_miles < 0  or end_miles > MAX_END:
                raise ValueError
            
    # Get a fuel amount in U.S. gallons from the user.
            amount_gallons = float(input("Enter the amount of fuel used (gallons): "))
            if amount_gallons < 0 or amount_gallons > MAX_FUEL:
                raise ValueError
            break
        except ValueError :
            # catch any invalid input and print an error message
            print("Invalid input. Please enter a valid number")
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(start_miles, end_miles ,amount_gallons)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Display the results for the user to see.
    print(f"{mpg:.2f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers ")
    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    mpg = (end_miles - start_miles) / amount_gallons
    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k = 235.215 / mpg
    return lp100k

# Call the main function so that
# this program will start executing.
main()
