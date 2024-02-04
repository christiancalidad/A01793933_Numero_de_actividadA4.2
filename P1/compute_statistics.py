
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
    stats_calculator = StatsCalculator(lines)
    stats_calculator.convert_mueric()
    stats_calculator.calculate_stats()

    elapsed_time = time.time()  - start_time

    print("Descriptive Statistics:")
    print(f"Mean: {stats_calculator.mean}")
    print(f"Median: {stats_calculator.median}")
    print(f"Mode: {stats_calculator.mode}")
    print(f"Standard Deviation: {stats_calculator.std}")
    print(f"Variance: {stats_calculator.variance}")
    print(f"Elapsed Time: {elapsed_time} seconds")

    with open(f"{file_name}_StatisticsResults.txt", "w",encoding='utf-8') as results_file:
        results_file.write("Descriptive Statistics:\n")
        results_file.write(f"Mean: {stats_calculator.mean}\n")
        results_file.write(f"Median: {stats_calculator.median}\n")
        results_file.write(f"Mode: {stats_calculator.mode}\n")
        results_file.write(f"Standard Deviation: {stats_calculator.std}\n")
        results_file.write(f"Variance: {stats_calculator.variance}\n")
        results_file.write(f"Elapsed Time: {elapsed_time} seconds\n")



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


class StatsCalculator:
    """Class that try to convert a list of strings into numeric values and calculate basic 
    statistics.
    """
    def __init__(self, lines):
        self.lines = lines
        self.numbers = None
        self.mean = None
        self.median = None
        self.mode = None
        self.variance = None
        self.std = None

    def convert_mueric(self):
        """Try to convert each element in a list into a float and store the result in a 
        class atribute
        """
        self.numbers = []
        for i in self.lines:
            try:
                self.numbers.append(float(i))
            except ValueError:
                print(f"Error: element {i} is not numeric")

    def calculate_stats(self):
        """Calculate the basic stats for the class numbers attribute
        """
        self.calculate_mean()
        self.calculate_median()
        self.calculate_mode()
        self.calculate_sd_var()

    def calculate_mean(self):
        """Calculate mean
        """
        self.mean = sum(self.numbers)/len(self.numbers)

    def calculate_median(self):
        """Calculate median
        """
        sorted_numbers = sorted(self.numbers)

        if len(self.numbers) % 2 == 0:
            self.median = (sorted_numbers[len(self.numbers)//2 - 1] +
                           sorted_numbers[len(self.numbers)//2]) / 2
        else:
            self.median = sorted_numbers[len(self.numbers)//2]

    def calculate_mode(self):
        """Calculate mode
        """
        frequency_dict = {}
        for number in self.numbers:
            if number in frequency_dict:
                frequency_dict[number] += 1
            else:
                frequency_dict[number] = 1
        max_freq = max(frequency_dict.values())
        if max_freq>1:
            self.mode = [number for number, freq in frequency_dict.items() if freq == max_freq][0]
        else:
            self.mode = "N/A"

    def calculate_sd_var(self):
        """_Calculate Standar Deviation and Variance
        """
        self.variance = sum((x - self.mean) ** 2 for x in self.numbers) / len(self.numbers)
        self.std = self.variance ** (0.5)



if __name__ == "__main__":
    main()
