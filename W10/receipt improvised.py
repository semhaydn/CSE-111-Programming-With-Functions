import csv
import sys
from datetime import datetime

PRODUCTNUMBERINDEX = 0
PRODUCTQUANTITYINDEX = 1
NAMEINDEX = 1
PRICEINDEX = 2

def main():
    try:
        product_file = "products.csv"
        request_file = "request.csv"

        # Read the product dictionary and request list
        products_dict = read_dictionary(product_file, PRODUCTNUMBERINDEX)
        request_list = read_request_list(request_file)

        # Print the receipt header
        print_receipt_header()

        # Print the requested items
        print_requested_items(request_list, products_dict)

        # Print the order summary
        print_order_summary(request_list, products_dict)

    except FileNotFoundError as e:
        print(f"File not found. Please check the file path and try again: {e.filename}")
    except PermissionError:
        print("Permission denied. Please ensure you have the necessary permissions.")

def read_dictionary(product_file, key_column_index):
    dictionary = {}
    try:
        with open(product_file, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[key_column_index]
                    dictionary[key] = row_list
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found. Please check the file path and try again: {e.filename}")
    except PermissionError:
        raise PermissionError("Permission denied. Please ensure you have the necessary permissions.")
    return dictionary

def read_request_list(request_file):
    request_list = []
    try:
        with open(request_file, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row_list in reader:
                if len(row_list) != 0:
                    request_list.append(row_list)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found. Please check the file path and try again: {e.filename}")
    except PermissionError:
        raise PermissionError("Permission denied. Please ensure you have the necessary permissions.")
    return request_list

def print_receipt_header():
    # Print receipt header information
    greeting = 'Thank you for choosing'
    store_name = "Mama John's"
    address_line1 = '3477 Broadway'
    address_line2 = 'New York, NY 10031'

    print('*' * 70)
    print(f'{"RECEIPT":^70}')
    print('*' * 70)
    print('\n')
    print(f'{greeting:^70}')
    print(f'{store_name:^70}')
    print(f'{address_line1:^70}')
    print(f'{address_line2:^70}')
    print('\n')
    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%a %b %e %H:%M:%S %Y}")
    print('*' * 70)
    print('\nRequested Items')

def print_requested_items(request_list, products_dict):
    total_quantity = 0
    for request in request_list:
        product_number = request[PRODUCTNUMBERINDEX]
        quantity = int(request[PRODUCTQUANTITYINDEX])
        try:
            product_info = products_dict[product_number]
            product_name = product_info[NAMEINDEX]
            product_price = float(product_info[PRICEINDEX])
            print(f"{product_name}: {quantity} @ {product_price}")
            total_quantity += quantity
            item_total = quantity * product_price
        except KeyError:
            print(f"Product with number {product_number} not found.")
            continue

def print_order_summary(request_list, products_dict):
    total_quantity = 0
    subtotal_due = 0.0
    sales_tax_rate = 0.06

    for request in request_list:
        product_number = request[PRODUCTNUMBERINDEX]
        quantity = int(request[PRODUCTQUANTITYINDEX])
        try:
            product_info = products_dict[product_number]
            product_name = product_info[NAMEINDEX]
            product_price = float(product_info[PRICEINDEX])
            total_quantity += quantity
            item_total = quantity * product_price
            subtotal_due += item_total
        except KeyError:
            continue

    sales_tax_amount = subtotal_due * sales_tax_rate
    total_due = subtotal_due + sales_tax_amount

    print(f"\nTotal Ordered Items: {total_quantity}")
    print(f"Subtotal Due: ${subtotal_due:.2f}")
    print(f"Sales Tax Amount: ${sales_tax_amount:.2f}")
    print(f"Total Amount Due: ${total_due:.2f}")
    points = int(total_due)
    print(f'\nYou earned {points} points! You can use your points on our webpage!')
    print('')
    print('')
    print('*' * 70)
    
    # Prompt for tip amount
    tip_percentage = float(input('Enter tip percentage (5, 10, or 15): '))
    tip_amount = total_due * (tip_percentage / 100)
    print(f'Tip amount: ${tip_amount:.2f}')
    total_with_tip = tip_amount + total_due

    print(f'Total Amount Due: {total_with_tip:.2f}')

    # Prompt for payment amount and calculate change
    payment_amount = float(input('What is the payment amount? '))
    while payment_amount < total_with_tip:
        print('Payment amount must be greater than or equal to total with tip.')
        payment_amount = float(input('What is the payment amount? '))
    change = payment_amount - total_with_tip
    print
    print(f'Change: ${change:.2f}')
    print(f"\nThank you for shopping at Mama John's!")
    print('*' * 70)

if __name__ == "__main__":
    main()
