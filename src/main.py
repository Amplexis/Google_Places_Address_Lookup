import os
from src.functions import create_output_file, fill_lists, build_row_and_write_to_outfile

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
df = pd.DataFrame(columns=["Passcode", "Agency", "Address_1", "Address_2"])
for i in range(0, len(passcodes)):
    pcode = passcodes[i]
    agency = agencies_orig[i]
    df = df.append({"Passcode":pcode, "Agency":agency}, ignore_index=True)
print(df)
writer = pd.ExcelWriter('test_output.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name="Sheet1", index=False)
writer.save()
# build_row_and_write_to_outfile(agencies_formatted, agencies_orig, passcodes, filepath_out)
#
# print("finished")
