#!/usr/bin/env python3
import pandas as pd
import sys

input_file = 'sales_2013.xlsx'
output_file = 'output_files/4output_pandas2.xlsx'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_value_meets_condition = \
	data_frame[data_frame['Sale Amount'] > 1400.0]
	# data_frame[data_frame['Sale Amount'].astype(float) > 1400.0]

writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()