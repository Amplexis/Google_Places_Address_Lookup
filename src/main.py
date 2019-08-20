import os
from src.functions import fill_lists, build_list_of_rows, create_header_row, adjust_row_length, build_data_frame, write_data_frame_to_file

infile = "sample_file.xlsx"
outfile = "output.xlsx"

base_dir = os.path.dirname(os.path.dirname(__file__))
filepath_in = os.path.join(base_dir, "input/", infile)
filepath_out = os.path.join(base_dir, "output/", outfile)

agencies_orig = []
agencies_formatted = []
passcodes = []

agencies_orig, passcodes, agencies_formatted = fill_lists(filepath_in, agencies_orig, passcodes, agencies_formatted)
max_results = 0
rows = []
headers = ["Passcode", "Agency"]

rows, max_results = build_list_of_rows(agencies_formatted, agencies_orig, passcodes, rows, max_results)

headers = create_header_row(headers, max_results)

rows = adjust_row_length(rows, headers)

df = build_data_frame(headers, rows)

write_data_frame_to_file(df, filepath_out)
