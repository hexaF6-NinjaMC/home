import csv
from datetime import datetime
import os
clear = lambda:os.system("cls")
clear()


def main():
    # For products.csv and request.csv:
    PRODUCT_NUMBER_INDEX = 0
    # For request.csv:
    QUANTITY_INDEX = 1
    # For products.csv:
    PRODUCT_NAME_INDEX = 1
    PRICE_INDEX = 2

    products = {}

    file = input("Enter the file (with extension) containing list of products: -- ")
    try:
        tax_rate = 0.06                 # 6% tax rate percentage as a float
        products = read_products(file, products, PRODUCT_NUMBER_INDEX, PRODUCT_NAME_INDEX, PRICE_INDEX)
        # products = read_products("products.csv", products, PRODUCT_NUMBER_INDEX, PRODUCT_NAME_INDEX, PRICE_INDEX)
        file = input("Enter the file (with extension) containing customer request(s): -- ")
        clear()
        print_receipt(file, products, PRODUCT_NUMBER_INDEX, QUANTITY_INDEX, tax_rate)
    except FileNotFoundError as file_nf_err:
        clear()
        print(f'File "{file}" not found in current directory.')
        print(file_nf_err)
        os._exit(0)
    except PermissionError as perm_err:
        clear()
        print(f"You do not have required access to {file}.")
        print(perm_err)
        os._exit(0)
    except KeyError as key_err:
        clear()
        print("Key not found.")
        print(type(key_err).__name__, key_err)
        os._exit(0)
    # Exceeding the requirements:
    except IndexError as index_err:
        clear()
        print("Index error.")
        print(f"{type(index_err).__name__}: {index_err}.")
        os._exit(0)
    except ValueError as val_err:
        clear()
        print(f"Value error:")
        print(f"    {val_err}.")
        os._exit(0)

def read_products(file_name, dictionary, prod_num_index, prod_name_index, price_index):
    with open(file_name, "rt") as file:
        next(file)
        reader = csv.reader(file)
        for row in reader:
            key = row[prod_num_index]
            value = [row[prod_name_index], float(row[price_index])]
            dictionary[key] = value
    return dictionary

def print_requests(file_name, dictionary, prod_num_index, quan_index):
    print("Requested Items")
    with open(file_name, "rt") as order_file:
        next(order_file)
        item_count = 0
        subtotal = 0.00
        for row in order_file:
            row = row.strip()
            row = row.split(sep=",")
            product_number = row[prod_num_index]
            product_name = dictionary[product_number][0]
            quantity = int(row[quan_index])
            price = float(dictionary[product_number][1])
            print(f"{product_name}: {quantity} @ {price}")
            item_subtotal = calculate_subtotal(quantity, price)
            subtotal += item_subtotal

            # Calculate the number of items sold.
            item_count += quantity
    subtotal = round(subtotal, 2)
    return item_count, subtotal

def calculate_subtotal(quantity, price):
    item_subtotal = quantity * price
    return item_subtotal

def calculate_tax(subtotal, tax_percentage):
    sales_tax = round(subtotal * tax_percentage, 2)
    return sales_tax

def calculate_total_due(subtotal, sales_tax=0.00):
    total_due = subtotal + sales_tax
    return total_due

def print_receipt(file, dictionary, prod_num_index, quan_index, tax_rate=0.00):
    # Print the store name at the top of the terminal window.
    print()
    print("Flash Goods - For Your Convenience")
    print()

    number_of_items_sold, subtotal = print_requests(file, dictionary, prod_num_index, quan_index)
    print()
    print(f"Number of Items: {number_of_items_sold}")
    print(f"Subtotal: {subtotal}")

    # Calculate and print the sales tax.
    sales_tax = calculate_tax(subtotal, tax_rate)
    print(f"Sales tax: {sales_tax}")

    # Calculate and print total due.
    total_due = calculate_total_due(subtotal, sales_tax)
    print(f"Total: {total_due}")
    print()
    print("Thank you for shopping at Flash Goods.")
    current_date = datetime.now()
    print(datetime.ctime(current_date))
    print()
    os._exit(0)


if __name__ == "__main__":
    main()