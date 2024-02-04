
"""This file is for calculating basic statistics from a given filename.
"""

import time
import sys


def main():
    """main function to orchestate the whole process
    """
    file_name = sys.argv[1]
    start_time = time.time()

    lines = read_file(file_name)
    for line in lines:
        try:
            number = int(line)
            binary = to_binary(number)
            hexadecimal = to_hexadecimal(number)
        except TypeError:
            number = line
            binary = '#VALUE!'
            hexadecimal = '#VALUE!'

        print(f"Number: {number}, Binary: {binary}, Hexadecimal: {hexadecimal}")
        with open(f"{file_name}_ConvertionResults.txt", 'a', encoding='utf-8') as output_file:
            output_file.write(f"Number: {number}, Binary: {binary}, Hexadecimal: {hexadecimal}\n")


    elapsed_time = time.time()  - start_time
    print(f"Elapsed Time: {elapsed_time} seconds")

    with open(f"{file_name}_ConvertionResults.txt", "a",encoding='utf-8') as output_file:
        output_file.write(f"Elapsed Time: {elapsed_time} seconds\n")



def to_binary(num):
    """Function to convert to binary
    """
    if num < 0:
        num = 2**32 + num
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

def to_hexadecimal(num):
    """Function to convert to hexadecimal
    """
    if num < 0:
        num = 2**32 + num
    hexadecimal = ""
    while num > 0:
        remainder = num % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(65 + remainder - 10) + hexadecimal
        num = num // 16
    return hexadecimal



def read_file(file_name):
    """Read a file and return a list of strings with each row
    """
    try:
        with open(file_name, 'r',encoding='utf-8') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines] # eliminate withspaces
        return lines
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None



if __name__ == "__main__":
    main()
