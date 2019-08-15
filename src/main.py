import os
import csv
import requests
import json
from src.functions import create_output_file, fill_lists

# infile = "sample_file.xlsx"
infile = "test_sample_file.xlsx"
outfile = "output.csv"

base_dir = os.path.dirname(os.path.dirname(__file__))
filepath_in = os.path.join(base_dir, "input/", infile)
filepath_out = os.path.join(base_dir, "output/", outfile)

create_output_file(filepath_out)

agencies_orig = []
agencies_formatted = []
passcodes = []

agencies_orig, passcodes, agencies_formatted = fill_lists(filepath_in, agencies_orig, passcodes, agencies_formatted)

print(agencies_orig)
print(passcodes)
print(agencies_formatted)

# KEY = 'YOUR_KEY'
# QUERY1 = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input='
# QUERY2 = '&fields=formatted_address,name&inputtype=textquery&key='
#
# for index, agency in enumerate(agencies):
#     print(index)
#     row = []
#     row.append(passcodes[index])
#     row.append(orig[index])
#     try:
#         response = requests.get(QUERY1 + agency + QUERY2 + KEY)
#         result = json.loads(response.content)
#         with open(filepath_out, 'a') as outfile:
#             writer = csv.writer(outfile)
#             if not len(result['candidates']) == 0:
#                 for i in range(len(result['candidates'])):
#                     row.append(result['candidates'][i]['formatted_address'])
#             else:
#                 row.append("NO RESULTS FOUND")
#             writer.writerow(row)
#     except Exception as e:
#         print(e)
#
# print("finished")
