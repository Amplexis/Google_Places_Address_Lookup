import pathlib
import csv
import pandas as pd
import string

def create_output_file(filepath_out):
    if not pathlib.Path(filepath_out):
        HEADERS = ["Passcode", "Agency", "Address_1", "Address_2", "Address_3", "Address_4", "Address_5\n"]
        with open(filepath_out, 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(HEADERS)

def fill_lists(filepath_in, agencies_orig, passcodes, agencies_formatted):
    with pd.ExcelFile(filepath_in) as xlsx:
        sample = pd.read_excel(xlsx)

        for i in sample.index:
            agencies_orig.append(sample["Agency"][i])
            passcodes.append(sample["Passcode"][i])
            agency = sample["Agency"][i]
            agency = format_agnecy_for_query(agency)
            agencies_formatted.append(agency)
        result = (agencies_orig, passcodes, agencies_formatted)
        return result

def format_agnecy_for_query(agency):
    agency = agency.translate(str.maketrans('', '', string.punctuation))
    agency = agency.replace(" ", "%20")
    return agency
