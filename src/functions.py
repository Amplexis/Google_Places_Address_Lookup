import csv
import pandas as pd
import string
import requests
import json


def create_output_file(filepath_out):
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


def build_row_and_write_to_outfile(agencies_formatted, agencies_orig, passcodes, filepath_out):
    for index, agency in enumerate(agencies_formatted):
        print("Processing index: " + str(index))
        row = []
        row.append(passcodes[index])
        row.append(agencies_orig[index])

        result = api_call(agency)
        if not len(result['candidates']) == 0:
            for i in range(len(result['candidates'])):
                row.append(result['candidates'][i]['formatted_address'])
        else:
            row.append("NO RESULTS FOUND")
        write_row_to_outfile(row, filepath_out)


def api_call(agency):
    KEY = 'YOUR_KEY'
    QUERY1 = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input='
    QUERY2 = '&fields=formatted_address,name&inputtype=textquery&key='
    try:
        response = requests.get(QUERY1 + agency + QUERY2 + KEY)
        result = json.loads(response.content)
        return result
    except Exception as e:
        print(e)


def write_row_to_outfile(row, filepath_out):
    with open(filepath_out, 'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(row)
