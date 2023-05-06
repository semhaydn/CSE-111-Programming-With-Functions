# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime

MAX_WEIGHT = 2000
MAX_HEIGHT = 200
convertion_rate_pounds_to_kg = 0.45359237 
convertion_rate_inches_to_cm = 2.54

def main():
    while True:
        try:
            # Get the user's gender.
            gender = input("Please enter your gender (M or F): ").lower()
            if gender not in ['m', 'f']:
                raise ValueError("Invalid gender. Please enter M or F.")
            
            # Get the user's birthdate.
            birth_str = input("Enter your birthdate (YYYY-MM-DD): ")

            # At this point, gender and birthdate contain valid values, so we can proceed with the rest of the program.
    
            # Get the user's height and weight.
            pounds = float(input("Enter your weight in U.S. pounds: "))
            if pounds < 0 or pounds > MAX_WEIGHT:
                raise ValueError("Invalid number. Please enter valid number")
            inches = float(input("Enter your height in U.S. inches: "))
            if inches < 0 or inches > MAX_HEIGHT:
                raise ValueError("Invalid number. Please enter valid number")
            # If we got here, the inputs are valid, so we can break out of the loop.
            break
        except ValueError as e:
            print(str(e))
    
    # Compute the user's age.
    age = compute_age(birth_str)
    
    # Compute the user's body mass index.
    weight = kg_from_lb(pounds)
    height = cm_from_in(inches)
    bmi = body_mass_index(weight,height)
    
    # Compute the user's basal metabolic rate.
    bmr = basal_metabolic_rate(gender,weight,height,age)

    # rounding the values
    weight = round(weight,2)
    height = round(height,2)
    bmi = round(bmi, 2)
    bmr = round(bmr, 2)
    
    # Print the results for the user to see.
    print(f"Age (Years): {age}")
    print(f"Weight (kg): {weight}")
    print(f"Height (cm): {height}")
    print(f"Body mass index: {bmi}")
    print(f"Basal metabolic rate (kcal/day): {bmr}")


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    weight = pounds * convertion_rate_pounds_to_kg

    return weight


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    height = inches * convertion_rate_inches_to_cm
    return height


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight) / (height ** 2)
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender == "m":
        bmr = 88.362 + (13.397* weight) + (4.799 * height) - (5.677 * age)
    if gender == "f":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 *age)

    return bmr


# Call the main function so that
# this program will start executing.
main()