import pandas as pd
from abc import ABC
from IReadFile import IReadFile

class ReadCSV(IReadFile):
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        num_header_lines = 5
        data = []
        # Open the CSV file in read mode
        with open(self.__filename, 'r',  encoding="utf8") as file:
            # dialect = csv.Sniffer().sniff(file.read(), [','])
            # file.seek(0)
            has_header = True # csv.Sniffer().has_header()

        

       
            # Create a CSV reader object
            csv_reader = pd.read_csv(file, skiprows=6)

            # Skip header lines
            # if has_header:
            #     for _ in range(num_header_lines):
            #         next(csv_reader)

            # Iterate over each row in the CSV file
            for row in csv_reader:
                 print(row["Book Name"])

      