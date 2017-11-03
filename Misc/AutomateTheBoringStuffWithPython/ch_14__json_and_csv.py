import csv, os, json

os.chdir('Misc/AutomateTheBoringStuffWithPython')

def exampleReadFile():
    exampleFile = open('example.csv')
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    print(exampleData)

def readLargeFileWithLoop():
    exampleFile = open('example.csv')
    exampleReader = csv.reader(exampleFile)

    for idx, row in enumerate(exampleReader):
        print(f"Row #{str(exampleReader.line_num)}:{str(row)} | idx:{idx}")

def writeFile():
    outFile = open('output.csv', 'w', newline='')
    outWriter = csv.writer(outFile)
    outWriter.writerow(['spam', 'monty', 'python', 'stuff'])
    outWriter.writerow(['spam', 'monty', 'python', 'stuff'])
    outWriter.writerow(list((1,2,3,4,5)))
    outFile.close()

def jsonLoad():
    # Convert JSON to Python Object
    jsonDataString = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
    data = json.loads(jsonDataString)
    print(data)

    # Convert Python Object to JSON String
    convertedJsonString = json.dumps(data)

# readLargeFileWithLoop()
# writeFile()
jsonLoad()