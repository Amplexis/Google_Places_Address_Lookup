import os
from src.functions import create_output_file, fill_lists, build_row_and_write_to_outfile, build_row_and_write_to_xlsx
from src.functions import api_call
import pandas as pd


infile = "sample_file.xlsx"
outfile = "output.csv"

base_dir = os.path.dirname(os.path.dirname(__file__))
filepath_in = os.path.join(base_dir, "input/", infile)
filepath_out = os.path.join(base_dir, "output/", outfile)

create_output_file(filepath_out)

agencies_orig = []
agencies_formatted = []
passcodes = []

agencies_orig, passcodes, agencies_formatted = fill_lists(filepath_in, agencies_orig, passcodes, agencies_formatted)
max_results = 0
rows = []
headers = ["Passcode", "Agency"]

for index, agency in enumerate(agencies_formatted):
    row = []
    row.append(passcodes[index])
    row.append(agencies_orig[index])

    result = api_call(agency)
    if len(result['candidates']) > max_results:
        max_results = len(result['candidates'])

    if not len(result['candidates']) == 0:
        for i in range(len(result['candidates'])):
            row.append(result['candidates'][i]['formatted_address'])
    else:
        row.append("NO RESULTS FOUND")

    rows.append(row)

print(rows)

for i in range(1, max_results+1):
    headers.append("Address_{}".format(i))

df = pd.DataFrame(columns=headers)
for i in range(0, len(rows)):
    df.loc[i] = rows[i]


print(df)
writer = pd.ExcelWriter('test_output.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name="Sheet1", index=False)
writer.save()


# build_row_and_write_to_outfile(agencies_formatted, agencies_orig, passcodes, filepath_out)
# print("finished")
