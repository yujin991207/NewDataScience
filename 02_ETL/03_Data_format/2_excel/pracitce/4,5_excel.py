from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = '../sales_2013.xls'
output_file = '../output_files/4output_basic_p.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

# 'sale_amount' 숫자없애려고
sale_amount_column_index = 3

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')

    data = []
    header = worksheet.row_values(0)
    data.append(header)