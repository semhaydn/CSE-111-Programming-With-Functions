from datetime import datetime

MAX_WEIGHT_LBS = 2000
MAX_HEIGHT_IN = 200
MAX_WEIGHT_KG = 907.185
MAX_HEIGHT_CM = 508
CONVERSION_RATE_LBS_TO_KG = 0.45359237 
CONVERSION_RATE_IN_TO_CM = 2.54

def validate_date(birth_str):
    try:
        birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date. Please enter in the format YYYY-MM-DD.")
    if birthdate > datetime.now():
        raise ValueError("Birthdate can't be in the future.")
    return birthdate

def validate_float(value, min_val, max_val):
    try:
        value = float(value)
    except ValueError:
        raise ValueError("Invalid number. Please enter a valid number.")
    if value < min_val or value > max_val:
        raise ValueError(f"Invalid number. Please enter a number between {min_val} and {max_val}.")
    return value

def get_user_data():
    while True:
        try:
            gender = input("Please enter your gender (M or F): ").lower()
            if gender not in ['m', 'f']:
                raise ValueError("Invalid gender. Please enter M or F.")

            birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
            birthdate = validate_date(birth_str)

            units = input("Enter the unit of measurement (M for Metric, I for Imperial): ").lower()
            if units not in ['m', 'i']:
                raise ValueError("Invalid option. Please enter M for Metric or I for Imperial.")

            if units == 'm':
                weight = validate_float(input("Enter your weight in kilograms: "), 0, MAX_WEIGHT_KG)
                height = validate_float(input("Enter your height in centimeters: "), 0, MAX_HEIGHT_CM)
            else:
                weight = validate_float(input("Enter your weight in pounds: "), 0, MAX_WEIGHT_LBS)
                height = validate_float(input("Enter your height in inches: "), 0, MAX_HEIGHT_IN)
                weight = kg_from_lb(weight)
                height = cm_from_in(height)

            return gender, birthdate, weight, height

        except ValueError as e:
            print(str(e))

def compute_age(birthdate):
    today = datetime.now()
    years = today.year - birthdate.year
    if birthdate.month > today.month or (birthdate.month == today.month and birthdate.day > today.day):
        years -= 1
    return years

def kg_from_lb(pounds):
    return pounds * CONVERSION_RATE_LBS_TO_KG

def cm_from_in(inches):
    return inches * CONVERSION_RATE_IN_TO_CM

def body_mass_index(weight, height):
    return (10000 * weight) / (height ** 2)

def bmi_classification(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def basal_metabolic_rate(gender, weight, height, age):
    if gender == "m":
        return 88.362 + (13.397* weight) + (4.799 * height) - (5.677 * age)
    if gender == "f":
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 *age)

def main():
    gender, birthdate, weight, height = get_user_data()
    age = compute_age(birthdate)
    bmi = body_mass_index(weight,height)
    bmi_class = bmi_classification(bmi)
    bmr = basal_metabolic_rate(gender,weight,height,age)
    print_results(age, weight, height, bmi, bmi_class, bmr)

def print_results(age, weight, height, bmi, bmi_class, bmr):
    print(f"Age (Years): {age}")
    print(f"Weight (kg): {round(weight, 2)}")
    print(f"Height (cm): {round(height, 2)}")
    print(f"Body mass index: {round(bmi, 2)} ({bmi_class})")
    print(f"Basal metabolic rate (kcal/day): {round(bmr, 2)}")

# Due to the interactive nature of the code (input()), this can't be run in the current environment.
# However, you can run this in your local Python environment by uncommenting the line below:

# Call main to start this program.
if __name__ == "__main__":
    main()
