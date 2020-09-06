import pandas as pd

excelfile = pd.ExcelFile('data4.xlsx')
dframe = excelfile.parse('Sheet1')
print(dframe)