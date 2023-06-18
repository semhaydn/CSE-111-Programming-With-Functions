import csv

def main():


    # name the csv files with a variable called filename
    product_file = "products.csv"

    request_file = "request.csv"

    PRODUCTNUMBERINDEX = 0
    NAMEINDEX = 1
    PRICEINDEX = 2


    # Calls the read_dictionary function and stores the compound dictionary in a variable named products_dict
    products_dict = read_dictionary(product_file,PRODUCTNUMBERINDEX)

    # Print the variable (dictionary)
    print("All products")
    print(products_dict)

    request_list = []

    with open(request_file , "rt") as csv_file:

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
            # If the current row is not blank,
            # append it to the request_list.
            if len(row_list) != 0:

                # Append one row from the CSV
                # file to the compound list.
                request_list.append(row_list)

        print('Requested Items')        









def read_dictionary(product_file, key_column_index):
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


    with open(product_file , "rt") as csv_file:

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

# Call main to start this program.
if __name__ == "__main__":
    main()