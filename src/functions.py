import pathlib
import csv

def create_output_file(filepath_out):
    if not pathlib.Path(filepath_out):
        HEADERS = ["Passcode", "Agency", "Address_1", "Address_2", "Address_3", "Address_4", "Address_5\n"]
        with open(filepath_out, 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(HEADERS)
