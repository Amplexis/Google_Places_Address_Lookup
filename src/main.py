import os
from src.functions import create_output_file, fill_lists, build_row_and_write_to_outfile

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
build_row_and_write_to_outfile(agencies_formatted, agencies_orig, passcodes, filepath_out)

print("finished")
