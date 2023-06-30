# Import the csv module so that it can be used
# to read from the accidents.csv file.
import csv


# Column numbers from the accidents.csv file.
YEAR_COLUMN = 0
FATALITIES_COLUMN = 1
INJURIES_COLUMN = 2
CRASHES_COLUMN = 3
FATAL_CRASHES_COLUMN = 4
DISTRACT_COLUMN = 5
PHONE_COLUMN = 6
SPEED_COLUMN = 7
DUI_COLUMN = 8
FATIGUE_COLUMN = 9


def main():
    # Entering to a loop for FileNotFoundError handling
    while True:
        try:
            # Prompt the user for a filename and open that text file.
            filename = input("Name of file that contains NHTSA data: ")
            with open(filename, "rt") as text_file: 
                
                # Entering to a loop for ZeroDivisionError abd ValueError handling
                while True:
                    try:
                        # Prompt the user for a percentage.
                        perc_reduc = float(input(
                            "Percent reduction of texting while driving [0, 100]: "))
                        
                        # Ensuring the input is between 0 and 100
                        if perc_reduc > 100 or perc_reduc < 0:
                            raise ZeroDivisionError('Percentage reduction must be between 0 and 100')
                        
                        # Leaving the loop if the value is correct
                        break

                        # # If the Error is occuring warning the user 
                    except ValueError :
                        print("Error: Invalid input. Please enter a valid percentage.")
                    except ZeroDivisionError as e:
                        print(f'Error : {e}')


                print()
                print(f"With a {perc_reduc}% reduction in using a cell",
                    "phone while driving, approximately the",
                    "following number of injuries and deaths",
                    "would have been prevented in the USA.", sep="\n")
                print()
                print("Year, Injuries, Deaths")

                # Use the csv module to create a reader
                # object that will read from the opened file.
                reader = csv.reader(text_file)

                # The first line of the CSV file contains column headings
                # and not a student's I-Number and name, so this statement
                # skips the first line of the CSV file.
                next(reader)

                # Process each row in the CSV file.
                for row in reader:
                    year = row[YEAR_COLUMN]

                    # Call the estimate_reduction function.
                    injur, fatal = estimate_reduction(
                            row, PHONE_COLUMN, perc_reduc)

                    # Print the estimated reductions
                    # in injuries and fatalities.
                    print(year, injur, fatal, sep=", ")

                # Leaving the main loop if the FileNotFoundError is occuring
                break

                # If the Error is occuring warning the user 
        except FileNotFoundError:
            print(f"File not found. Please check the file path and try again. : {filename} ")


          


def estimate_reduction(row, behavior_key, perc_reduc):
    """Estimate and return the number of injuries and deaths that
    would not have occurred on U.S. roads and highways if drivers
    had reduced a dangerous behavior by a given percentage.

    Parameters
        row: a CSV row of data from the U.S. National Highway Traffic
            Safety Administration (NHTSA)
        behavior_key: heading from the CSV file for the dangerous
            behavior that drivers could reduce
        perc_reduc: percent that drivers could reduce a dangerous
            behavior
    Return: The number of injuries and deaths that may have been
        prevented
    """
    behavior = int(row[behavior_key])
    fatal_crashes = int(row[FATAL_CRASHES_COLUMN])
    ratio = perc_reduc / 100 * behavior / fatal_crashes

    fatalities = int(row[FATALITIES_COLUMN])
    injuries = int(row[INJURIES_COLUMN])

    reduc_fatal = int(round(fatalities * ratio, 0))
    reduc_injur = int(round(injuries * ratio, 0))
    return reduc_injur, reduc_fatal


# If this file was executed like this:
# > python accidents.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
