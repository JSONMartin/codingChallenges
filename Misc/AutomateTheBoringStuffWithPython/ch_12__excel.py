import openpyxl

FILE_LOCATION = '/Users/jmartin/code/codingChallenges/Misc/AutomateTheBoringStuffWithPython/' + 'example.xlsx'
workbook = openpyxl.load_workbook(FILE_LOCATION)

sheet = workbook.get_sheet_by_name('Sheet1')

cells = tuple(sheet['A1':'C3'])

for rowOfCellObjects in cells:
    for cell in rowOfCellObjects:
        print(f"{cell.coordinate}:{cell.value}")


print('hi')