
"""This file is for calculatint total cost from a given list of
products and its prices
"""

import time
import sys
import json
import pandas as pd


def main():
    """main function to orchestate the whole process
    """
    start_time = time.time()

    catalogue_file = sys.argv[1]
    sales_file = sys.argv[2]

    dict_catalogue = read_file(catalogue_file)
    dict_sales = read_file(sales_file)

    df_products = pd.DataFrame(dict_catalogue)
    df_products = df_products[['title', 'price']]
    df_products.rename({'title': 'Product', 'price': 'Price'},
                       axis=1, inplace=True)

    df_sales = pd.DataFrame(dict_sales)

    list_missing_products = [
        i for i in df_sales.Product.to_list()
        if i not in df_products.Product.tolist()
        ]

    if len(list_missing_products) > 0:
        for i in list_missing_products:
            print(f'Error: product {i} not found in the catalogue')

    df_sales = df_sales.merge(df_products, how='inner', on='Product')
    df_sales['Subtotal'] = df_sales['Quantity'] * df_sales['Price']
    grand_total = df_sales['Subtotal'].sum()
    elapsed_time = time.time() - start_time

    print("Result:")
    print(df_sales)
    print("_______________________________________________________")
    print(f'Gran total: {grand_total}')
    print("_______________________________________________________")
    print(f"Elapsed Time: {elapsed_time} seconds")
    with open("SalesResults.txt", "w", encoding='utf-8') as results_file:
        results_file.write("Result:\n")
        results_file.write(df_sales.to_string())
        results_file.write("\n____________________________________________\n")
        results_file.write(f"Gran total: {grand_total}\n")
        results_file.write("______________________________________________\n")
        results_file.write(f"Elapsed Time: {elapsed_time} seconds\n")


def read_file(file_name):
    """Read a json file and return a dict with its content
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            dict_json = json.load(file)
        return dict_json
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None


if __name__ == "__main__":
    main()
