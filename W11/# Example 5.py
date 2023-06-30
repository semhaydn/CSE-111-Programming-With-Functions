# Example 5

def main():
    # Read a file that contains a list
    # of Canadian province names.
    provinces_list = read_file("provinces.txt")

    # As a debugging aid, print the entire list.
    print("Original list of provinces:")
    print(provinces_list)
    print()

    # Define a nested function that converts AB to Alberta.
    def alberta_from_ab(province_name):
        if province_name == "AB":
            province_name = "Alberta"
        return province_name

    # Replace all occurrences of "AB" with "Alberta" by
    # calling the map function and passing the ablerta_from_ab
    # function and provinces_list into the map function.
    new_list = list(map(alberta_from_ab, provinces_list))
    print("List of provinces after AB was changed to Alberta:")
    print(new_list)
    print()

    # Define a lambda function that returns True if a
    # province's name is Alberta and returns False otherwise.
    is_alberta = lambda name: name == "Alberta"

    # Filter the new list to only those provinces that
    # are "Alberta" by calling the filter function and
    # passing the is_alberta function and new_list.
    filtered_list = list(filter(is_alberta, new_list))
    print("List filtered to Alberta only:")
    print(filtered_list)
    print()

    # Because all the elements in filtered_list are
    # "Alberta", we can count how many elements are
    # "Alberta" by simply calling the len function.
    count = len(filtered_list)

    print(f"Alberta occurs {count} times in the modified list.")

def read_file(file):
    # Create an empty list that will store
    # the lines of text from the text file.
    list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open("provinces.txt", "rt") as text_file:

            # Read the contents of the text
            # file one line at a time.
            for line in text_file:
                # Remove white space, if there is any,
                # from the beginning and end of the line.
                clean_line = line.strip()

                # Append the clean line of text
                # onto the end of the list.
                list.append(clean_line)

    return list


# Call main to start this program.
if __name__ == "__main__":
    main()