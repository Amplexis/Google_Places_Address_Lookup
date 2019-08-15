import os
import pandas as pd
import string
import csv
import requests
import json

infile = "test_sample_file.xlsx"
outfile = "output.csv"

base_dir = os.path.dirname(os.path.dirname(__file__))
filepath_in = os.path.join(base_dir, "input/", infile)
filepath_out = os.path.join(base_dir, "output/", outfile)

orig = []
agencies = []
passcodes = []
with pd.ExcelFile(filepath_in) as xlsx:
    sample = pd.read_excel(xlsx)

    for i in sample.index:
        orig.append(sample["Agency"][i])
        passcodes.append(sample["Passcode"][i])
        agency = sample["Agency"][i]
        agency = agency.translate(str.maketrans('', '', string.punctuation))
        agency = agency.replace(" ", "%20")
        agencies.append(agency)

KEY = 'YOUR_KEY'
QUERY1 = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input='
QUERY2 = '&fields=formatted_address,name&inputtype=textquery&key='

for agency in agencies:
    response = requests.get(QUERY1 + agency +QUERY2+KEY)
    result = json.loads(response.content)

