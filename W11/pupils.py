import csv



# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():

    filename = "pupils.csv"

    student_list = read_compound_list(filename)

    # print(student_list)

    # Define a lambda function that will be used as the
    # key function by the sorted function. The lambda
    # function extracts the population data from a
    # pupil so that the birthdate will be used for
    # sorting the list of countries.

    birthdate_func = lambda pupil: pupil[SURNAME_INDEX]

    # Sort the list of pupils by the birthdate.
    sorted_list = sorted(student_list, key=birthdate_func)

    # Can use built in map function to print sorted lines easily
    # print("List of pupils sorted by birthday")
    # # list(map(print,sorted_list))

    # Print the sorted list.
    print("List of pupils sorted by birthday")
    print_list(sorted_list)



def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)
    
    return compound_list


def print_list (sorted_list):
   # Using build in map function to eleminate creating for loop
   list(map(print,sorted_list))



# Call main to start this program.
if __name__ == "__main__":
    main()