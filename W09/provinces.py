
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

def main():

    text_list = read_file("provinces.txt")
    # Print the entire list.
    print(text_list)

    # Remove the first element from the list.
    text_list.pop(0)

    # Remove the last element from the list.
    text_list.pop()

    # Replace all occurrences of "AB" in the list with "Alberta".
    value_to_replace = "AB"
    new_value = "Alberta"

    for i in range(len(text_list)):
        if text_list[i] == value_to_replace:
            text_list [i] = new_value

    # Count the number of elements that are "Alberta" and print that number.
    count = text_list.count("Alberta")
    print()
    print(f"Alberta occurs {count} times in the modified list.")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()






    