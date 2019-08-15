import os
import pandas as pd

infile = "sample_file.xlsx"
outfile = "output.csv"

base_dir = os.path.dirname(os.path.dirname(__file__))
filepath_in = os.path.join(base_dir, "input/", infile)
filepath_out = os.path.join(base_dir, "output/", outfile)

with pd.ExcelFile(filepath_in) as xlsx:
    sample = pd.read_excel(xlsx)

    for i in sample.index:
        agency = (sample["Agency"][i])