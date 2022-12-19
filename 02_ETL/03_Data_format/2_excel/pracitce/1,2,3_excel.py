from xlrd import open_workbook
from xlwt import Workbook

input_file = '../sales_2013.xls'
output_file = '../output_files/2output_basic.xls'

workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)

for worksheet in workbook.sheets():
    print('Worksheet name:', worksheet.name, "\tRows:",
          worksheet.nrows, "\tColumns:", worksheet.ncols)

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')

    #for row_index in range(worksheet.nrows):
        #for column_index in range(worksheet.ncols):
