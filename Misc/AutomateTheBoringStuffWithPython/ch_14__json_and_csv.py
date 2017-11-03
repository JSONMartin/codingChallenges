import csv, os

os.chdir('Misc/AutomateTheBoringStuffWithPython')

def exampleReadFile():
    exampleFile = open('example.csv')
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    print(exampleData)

exampleReadFile()