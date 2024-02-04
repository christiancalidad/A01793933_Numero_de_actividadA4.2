
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
    lines = [str(line).strip() for line in lines]
    word_counts = {}
    for line in lines:
        words = line.split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    for word, count in word_counts.items():
        print(f"{word}  {count}")
    word_counts = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))
    # Guardar resultados en un archivo
    with open(f"{file_name}_WordCountResults.txt", 'a',encoding='utf-8') as output_file:
        for word, count in word_counts.items():
            output_file.write(f"{word}  {count}\n")
        elapsed_time = time.time()  - start_time
        print(f"Elapsed Time: {elapsed_time} seconds")
        output_file.write(f"Elapsed Time: {elapsed_time} seconds\n")


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
