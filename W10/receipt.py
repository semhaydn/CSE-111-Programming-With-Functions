import csv
import sys
# Import the time
from datetime import datetime

def main():
    
    try:
        product_file = "products.csv"
        request_file = "request.csv"
        # name the csv files with a variable called filename


        PRODUCTNUMBERINDEX = 0
        PRODUCTQUANTITYINDEX = 1
        NAMEINDEX = 1
        PRICEINDEX = 2
        # Calls the read_dictionary function and stores the compound dictionary in a variable named products_dict
        products_dict = read_dictionary(product_file,PRODUCTNUMBERINDEX)


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

        # A warm welcome to customer
        greeting = 'Thank you for choosing'

        # information about the company
        store_name = "Mama John's"
        address_line1 = '3477 Broadway'
        address_line2 = 'New York, NY 10031'

        # We will use "*" To seperate the parts of the receipt
        print('*' * 70)

        # Header
        print(f'{"RECEIPT":^70}')

        # We will use "*" To seperate the parts of the receipt
        print('*' * 70)

        # Blank Space
        print('\n')

        # Displaying the greeting and information about the store
        print(f'{greeting:^70}')
        print(f'{store_name:^70}')
        print(f'{address_line1:^70}')
        print(f'{address_line2:^70}')

        # Blank Space
        print('\n')

        # Prompting the date
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%a %b %e %H:%M:%S %Y}")

        # We will use "*" To seperate the parts of the receipt
        print('*' * 70)
        # Print the header for the requested items
        print('\nRequested Items')

        # Iterate over each request in the request list
        try:
            total_quantity = 0  # Variable to store the total quantity
            subtotal_due = 0.0  # Variable to store the subtotal due
            sales_tax_rate = 0.06  # Sales tax rate (6%)

            for request in request_list:
                # Extract the product number and quantity from the request
                product_number = request[PRODUCTNUMBERINDEX]
                quantity = int(request[PRODUCTQUANTITYINDEX])

                try:
                    # Retrieve the product information from the products dictionary
                    product_info = products_dict[product_number]
                    product_name = product_info[NAMEINDEX]
                    product_price = float(product_info[PRICEINDEX])

                    # Print the product name, quantity, and price
                    print(f"{product_name}: {quantity} @ {product_price}")
                    total_quantity += quantity  # Add the quantity to the total.

                    item_total = quantity * product_price  # Calculate the total cost for the item
                    subtotal_due += item_total  # Add the item total to the subtotal

                except KeyError:
                    print(f"Product with number {product_number} not found.")
                    continue  # Skip the rest of the loop for this request

            sales_tax_amount = subtotal_due * sales_tax_rate  # Calculate the sales tax amount
            total_due = subtotal_due + sales_tax_amount  # Calculate the total amount due

            print(f"\nTotal Ordered Items: {total_quantity}") # Print the total quantity of items that are requested
            print(f"Subtotal Due: ${subtotal_due:.2f}") # printing the total before the tax
            print(f"Sales Tax Amount: ${sales_tax_amount:.2f}") # printing the sale tax amount
            print(f"Total Amount Due: ${total_due:.2f}") # Printing the total due

            # Adding point system
            points = int(total_due)
            print(f'\nYou earned {points} points! You can use your points on our webpage!')

            # leaving empty spaces
            print('')
            # leaving empty spaces
            print('')

            # We will use "*" To seperate the parts of the receipt
            print('*' * 70)

            # Adding tip system
            # Prompting the tip percentage from the user
            tip_percentage = float(input('Enter tip percentage (5, 10, or 15): '))

            # Calculating the tip amount based on the total due
            tip_amount = total_due * (tip_percentage / 100)
            print(f'Tip amount: ${tip_amount:.2f}')

            # leaving empty spaces
            print('')

            # Calculating the total with tip
            total_with_tip = total_due + tip_amount

            # Displaying the total with tip
            print(f'Total with tip amount: ${total_with_tip:.2f}')

            # Payment Amount
            # Prompting the payment amount from the user
            payment_amount = float(input('What is the payment amount? '))

            # Validating the payment amount
            while payment_amount < total_with_tip:
                print('Payment amount must be greater than or equal to total with tip.')
                payment_amount = float(input('What is the payment amount? '))

            # Calculating the change
            change = payment_amount-total_with_tip

            # Displaying the change
            print(f'Change: ${change:.2f}')

            # Printing a thank you to the customer
            print(f'\nThank you for shopping at the {store_name}')

            # We will use "*" To seperate the parts of the receipt
            print('*' * 70)

        except FileNotFoundError:
            print(f"File not found. Please check the file path and try again.{request_file}")

    except PermissionError:
        print("Permission denied. Please ensure you have the necessary permissions.")

def read_dictionary(product_file, key_column_index):
    """Read the contents of a CSV file into a compound dictionary and return the dictionary.

    Parameters:
        product_file (str): The name of the CSV file to read.
        key_column_index (int): The index of the column to use as the keys in the dictionary.

    Returns:
        dict: A compound dictionary that contains the contents of the CSV file,
              or None if the file is not found or an error occurs.
    """
    # Create an empty dictionary that will store the data from the CSV file.
    dictionary = {}

    try:
        with open(product_file, "rt") as csv_file:
            # Use the csv module to create a reader object that will read from the opened file.
            reader = csv.reader(csv_file)

            # Skip the header row
            next(reader)

            # Read the rows in the CSV file one row at a time.
            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[key_column_index]
                    dictionary[key] = row_list

    except FileNotFoundError:
        print(f"File not found. Please check the file path and try again. : {product_file} ")
        sys.exit(1)  # Exit the program with a non-zero exit code

    except PermissionError:
        print("Permission denied. Please ensure you have the necessary permissions.")
        sys.exit(1)  # Exit the program with a non-zero exit code

    return dictionary

# Call main to start this program.
if __name__ == "__main__":
    main()