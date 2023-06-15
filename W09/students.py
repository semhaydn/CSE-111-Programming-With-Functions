import csv

def main():

    # Get an I-number from the user
    i_number = input('Please enter an I-Number (xxxxxxxxx):')

    INUMBERINDEX = 0
    NAMEINDEX = 1


    # Read the contents of the CSV file into a dictionary
    student_name  = read_dictionary("students.csv", INUMBERINDEX)

    if i_number in student_name:

        value = student_name[i_number]
        name = value[NAMEINDEX]

        print(name)

    else:
        print('Student not found')

    
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}


    with open(filename , "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)


        # The first row of the CSV file contains column
        # headings and not data about a dental students,
        # so this statement skips the first row of the
        # CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list

    # Return the dictionary.
    return dictionary

if __name__ == '__main__':
    main()

